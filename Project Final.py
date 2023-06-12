import pandas as pd
import networkx as nx
import math

flights = "flights.csv"
hotels = "hotels.csv"
users = "users.csv"
name = input("Enter your name: ")
budget = float(input("Enter your budget: "))
num_cities = int(input("Enter the number of cities you want to visit: "))

def shortest_paths_dijkstras(budget, num_cities, graph, hotels, flights):
    cities = []
    current_budget = budget
    visited_cities = {}  # Dictionary to store visited cities, with city (to) as key and distance and cost as values.

    # Initialize the distance and cost dictionaries
    # Setting them to infinity at first as we don't know the distance from the closest city to the farthest.
    distance = {node: math.inf for node in graph.nodes}
    cost = {node: math.inf for node in graph.nodes}

    # Set the distance and cost of the start node to 0
    distance['start'] = 0
    cost['start'] = 0

    # Use dynamic programming to find the shortest paths and costs
    for i in range(len(graph.nodes) - 1): # Length of graphs, edges of graph
        for u, v, w in graph.edges(data='weight'):# u is the source node, v is the destination node, w represents the weight
            if distance[u] != math.inf and cost[u] + w < cost[v]: # Preventing infinite loops
                distance[v] = distance[u] + w
                cost[v] = cost[u] + w
    # Conter variable to insure iterating through all indexes!!
    counter = 0
    # Iterate over the nodes and find the cities to visit
    for node in graph.nodes:
        if node != 'start' and node != 'end':
            counter += 1
            if node in hotels['place'].values and node in flights['to'].values:
                # Filter hotels dataframe by place and days columns
                hotel_row = hotels.loc[(hotels['place'] == node) & (hotels['days'] == 2)]
                if not hotel_row.empty:
                    hotel_price = hotel_row['total'].values[counter]
                    flight_price = flights.loc[flights['to'] == node, 'price'].values[counter]
                    total_cost =  hotel_price + flight_price
                    if total_cost <= current_budget:
                        if node in visited_cities:
                            # Update visited_cities with the smallest distance and price
                            if distance[node] < visited_cities[node]['distance'] or (
                                    distance[node] == visited_cities[node]['distance'] and flight_price < visited_cities[node]['flight_price']):
                                visited_cities[node]['distance'] = distance[node]
                                visited_cities[node]['flight_price'] = flight_price
                                visited_cities[node]['hotel_price'] = hotel_price
                        else:
                            visited_cities[node] = {
                                'distance': distance[node],
                                'cost': cost[node] + flight_price,
                                'flight_price': flight_price,
                                'hotel_price': hotel_price
                            }
                        cities.append((node, total_cost))
                        current_budget -= total_cost
                        if len(cities) == num_cities:
                            break
    return cities, distance, cost, visited_cities
#O(N*M)
# Function to create a weighted graph from flights and hotels CSV files
def create_graph(flights, hotels):
    flights_data = pd.read_csv(flights)
    hotels_data = pd.read_csv(hotels)
    # Create an empty graph
    graph = nx.Graph()
    # Add start and end nodes to the graph
    graph.add_node('start')
    graph.add_node('end')

    # Iterate over flights data and add edges with weights to the graph
    for i, row in flights_data.iterrows():
        source = row['from']
        destination = row['to']
        distance = float(row['distance'])
        price = float(row['price'])
        weight = distance   # Calculating the weight using distance and price
        graph.add_edge(source, destination, weight=weight)

    # Add edges from start node to all cities
    for node in graph.nodes:
        if node != 'start' and node != 'end':
            graph.add_edge('start', node, weight=0)
    # Add edges from all cities to end node
    for node in graph.nodes:
        if node != 'start' and node != 'end':
            graph.add_edge(node, 'end', weight=0)

    # Call shortest_paths_dijkstras function to get cities within budget and number of cities
    cities, visited_distance, visited_cost, visited_cities = shortest_paths_dijkstras(budget, num_cities, graph, hotels_data, flights_data)

    if budget <= 675:
        print("The given budget is insufficient to visit any city.")
    elif num_cities > len(visited_cities):
        print("The number of cities exceeds the cities included in the database, which means you can easily visit all cities!")
    elif visited_cities:
        for city, cost in cities:
            print(f"City: {city}, Cost: {cost}")
    else:
        print("The given budget is insufficient to visit any city.")
#O(N)
#Overall O(N*M)
create_graph(flights, hotels)

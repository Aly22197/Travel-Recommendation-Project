import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Function to create a weighted graph from flights and hotels CSV files
def create_graph(flights_file, hotels_file):
    # Create an empty graph
    graph = nx.Graph()

    # Read flights CSV file
    flights_data = pd.read_csv(flights_file)
    for _, row in flights_data.iterrows():
        source = row['from']
        destination = row['to']
        distance = float(row['distance'])
        price = float(row['price'])
        value = distance / (price + 1)  # Calculating the value using distance and price
        graph.add_edge(source, destination, weight=distance, value=value)

    # Read hotels CSV file
    hotels_data = pd.read_csv(hotels_file)
    for _, row in hotels_data.iterrows():
        place = row['place']
        total = float(row['total'])
        if place in graph.nodes:
            graph.nodes[place]['value'] = total

    return graph

# Main program
if __name__ == '__main__':
    flights_file = 'flights.csv'
    hotels_file = 'hotels.csv'

    # Create the graph
    graph = create_graph(flights_file, hotels_file)

    # Draw the graph
    nx.draw(graph, with_labels=True)
    plt.show()

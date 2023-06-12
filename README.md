# Travel-Recommendation-Project
From a tourism company's data, find the maximum number of cities you can visit within a given budget.

Travel Recommendation Project

Program Requirements: -
1-	Input  Name, Budget, Number of Cities to be visited.
2-	Output  Recommended cities.
Algorithm: -
Solving the issue of recommending the maximum number of cities within the given data set, required to be split into smaller problems, solving them leads to reaching the required output which is the maximum number of cities.
First, we extract our data from our csv files. To extract them, using the Pandas module, we initialize the values of the variables (flights, hotels, users) with their corresponding files.
We move on to the next step which is the main algorithm used to calculate the maximum number of cities you can visit, within the budget given by the user.
For the algorithm I’m using graphs as the main data structure of our dataset, as the idea to utilize the Dijkstra’s algorithm to find the minimum path between nodes. By finding the minimum path, it gives us the minimum distance between each city, which finally results in the cheapest flight price.
Shortest_Path_dijkstra function: -
The function called shortest_path_dijkstras starts with taking the budget, number of cities, the graph, the hotel file, the flights file all as its arguments.
We initialize the cities list which contains our final outputted optimal cities, our budget, and our memorization dictionary (visited_cities), the dictionary carries our city names that we visit as its keys, and the value of these keys are the distance and price of the flights, by constantly updating the values through looping through the graph, we find the optimal output, which is the smallest distance between each node (city) at the cheapest price. This also helps in not needing to go through all paths provided in the dataset. Which saves a lot of time. The complexity of this function is O(N*M) time. Where N is length of the graph and M is the weight.
Create_Graph function: -
The use of the module networkx to facilitate the graph creation and addition of the nodes, edges, and weights.
The function create_graph takes our files (flights,hotels) as arguments, reads our dataset using the pandas module, and creates a graph with the nodes start, end. Then iterates over the flights file to get the source which is the next node after start ( “from” column), to the destination node ( “to” column),  by converting the datatype of distance and price to float values and calculating the weight of the edge then connecting the start and end nodes to all the cities. We call back the Dijkstra function to finally loop over the dataset columns and reach our final output of cities and the respective cost of the trip, utilizing some conditions to print the proper out and handling cases shown in the test cases.
The complexity of the function is O(N) time. Where N is the column needed.
Test Cases: -
1)	By using the inputs Aly, 5000,2 the output should be 2 cities with their respective costs.
 
2)	By using the inputs Aly, 500,2, the output should be the condition handled where the cities have no values because the budget is much less than the required amount to even go to one place.
 
3)	By using the inputs Aly, 5000000,20 the output should be the condition handled where the number of cities given in the input is much larger than all the data set citied provided.


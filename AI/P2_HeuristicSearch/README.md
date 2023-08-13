# P2_Heuristic Search

The problem implemented is the traveling salesman problem. The heuristic used is the nearest neighbor (NN) heuristic.

The nearest neighbour algorithm was one of the first algorithms used to solve the travelling salesman problem approximately. In that problem, the salesman starts at a random city and repeatedly visits the nearest city until all have been visited. The algorithm quickly yields a short tour, but usually not the optimal one.

These are the steps of the algorithm:

1.Initialize all vertices as unvisited.
2.Select an arbitrary vertex, set it as the current vertex u. Mark u as visited.
3.Find out the shortest edge connecting the current vertex u and an unvisited vertex v.
4.Set v as the current vertex u. Mark v as visited.
5.If all the vertices in the domain are visited, then terminate. Else, go to step 3.
6.The sequence of the visited vertices is the output of the algorithm.

The nearest neighbor algorithm is easy to implement and executes quickly, but it can sometimes miss shorter routes which are easily noticed with human insight, due to its "greedy" nature. As a general guide, if the last few stages of the tour are comparable in length to the first stages, then the tour is reasonable; if they are much greater, then it is likely that much better tours exist. Another check is to use an algorithm such as the lower bound algorithm to estimate if this tour is good enough.
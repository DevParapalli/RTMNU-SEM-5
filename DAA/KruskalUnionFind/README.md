# P4_KruskalUnionFind

**Kruskal's Algorithm:**

Kruskal's Algorithm is a greedy algorithm that constructs a Minimum Spanning Tree by iteratively adding edges to the MST in ascending order of their weights until all vertices are included, and no cycle is formed. Here are the steps of Kruskal's Algorithm:

1. **Initialization**: Create a set (or forest) containing all the vertices from the original graph, initially treating each vertex as a separate component.

2. **Sort Edges**: Sort all the edges of the graph in non-decreasing order of their weights.

3. **Iterate through Edges**: Starting from the edge with the smallest weight, iterate through the sorted edges.

4. **Edge Selection**: For each edge, check if adding it to the MST would create a cycle. If adding the edge does not create a cycle (i.e., the two vertices of the edge belong to different components), then add the edge to the MST, and merge the two components into one.

5. **Repeat**: Continue this process until you have added (V - 1) edges to the MST, where V is the number of vertices in the original graph.

6. **Result**: The resulting set of edges is the Minimum Spanning Tree of the original graph.

**Union-Find (Disjoint-Set) Data Structure:**

The Union-Find data structure is used to efficiently manage the connectivity information of the vertices while implementing Kruskal's Algorithm. It maintains a collection of disjoint sets, where each set represents a connected component. The Union-Find data structure supports two primary operations:

1. **Union (Merge)**: Merge two disjoint sets into one by connecting them. This operation is used when you add an edge to the MST to merge the two components it connects.

2. **Find (Find Representative)**: Given a vertex, find the representative (or root) of the set to which the vertex belongs. This operation is used to check whether two vertices belong to the same component when considering whether adding an edge forms a cycle.

The Union-Find data structure is typically implemented using two main techniques: "union by rank" and "path compression." These techniques help ensure efficient operations and maintain a balanced tree structure within each set.


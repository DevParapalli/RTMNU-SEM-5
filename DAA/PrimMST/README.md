# PrimMST

Prim's algorithm is a greedy algorithm used to find a minimum spanning tree in a connected graph. A minimum spanning tree is a subgraph that includes all the vertices of the original graph while minimizing the sum of the edge weights. This algorithm is widely used in network design, such as for constructing efficient road networks and connecting computer networks.

Prim's algorithm starts with an arbitrary node as the initial MST and incrementally adds edges to connect it to other nodes while maintaining the minimum total edge weight. The basic steps of Prim's algorithm are as follows:

1. Initialize an empty set to represent the MST.
2. Choose an arbitrary node (the starting point).
3. Find the minimum-weight edge that connects a node in the MST to a node outside the MST.
4. Add the selected edge and the associated node to the MST.
5. Repeat steps 3 and 4 until all nodes are included in the MST.

```plaintext
function Prim(Graph):
    Initialize an empty set MST to store the minimum spanning tree.
    Select an arbitrary starting node s and add it to MST.
    
    while MST does not contain all nodes in Graph:
        Find the minimum-weight edge (u, v) such that u is in MST and v is not in MST.
        Add v to MST, along with edge (u, v).
    
    return MST
```

# HuffmanCoding

Huffman coding is a widely used technique in computer science and information theory for lossless data compression. It was developed by David A. Huffman in 1952. Huffman coding assigns variable-length codes to input symbols (e.g., characters in a text file) in such a way that more frequently occurring symbols are assigned shorter codes, while less frequently occurring symbols are assigned longer codes. This results in efficient data compression, as common symbols are represented with fewer bits than rare symbols.

Here's an explanation of how Huffman coding works and its implementation:

1. **Frequency Counting**:
   - To create a Huffman code, the first step is to count the frequency of each symbol (or character) in the input data. This information is used to determine the code lengths later.

2. **Building a Huffman Tree**:
   - Create a priority queue (usually implemented as a min-heap) containing nodes for each symbol, with the frequency of that symbol as the key. Each node initially represents a single symbol.

   - Repeat the following steps until only one node remains in the priority queue:
     a. Remove the two nodes with the lowest frequencies from the queue.
     b. Create a new node with a frequency equal to the sum of the frequencies of the two nodes removed in step (a). This new node becomes the parent of the two nodes.
     c. Insert the new node back into the priority queue.

   - The final node in the priority queue is the root of the Huffman tree.

3. **Assigning Codes**:
   - Traverse the Huffman tree from the root to each leaf node (representing a symbol). Assign a '0' when you move left in the tree and a '1' when you move right. The resulting path from the root to each leaf node forms the binary code for that symbol.

4. **Generate Huffman Codes**:
   - After assigning codes to all symbols, you have a mapping of each symbol to its corresponding Huffman code. This mapping can be used to compress and decompress data.

Let's see an example of Huffman coding for the following set of symbols and their frequencies:

```txt
Symbol    Frequency
A         5
B         9
C         12
D         13
E         16
F         45
```

1. Build the Huffman tree:
    ```txt
               [100]
              /     \
           [45]      [55]
           /   \     /   \
         [A:5] [F:45] [B:9] [C:12, D:13, E:16]
    ```

2. Assign codes:
   - A: 1000
   - B: 1001
   - C: 101
   - D: 110
   - E: 111
   - F: 0

So, for example, 'A' is represented as '1000', 'F' is represented as '0', and so on.

In implementation, you can use various data structures, such as priority queues or heaps, to efficiently build the Huffman tree. Once the tree is constructed, you can create a lookup table for quick encoding and decoding. The encoded data is typically stored as a sequence of bits, which can be written to a file or transmitted over a network and then decoded using the same Huffman tree.
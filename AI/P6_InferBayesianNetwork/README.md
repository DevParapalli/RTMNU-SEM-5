# P6_InferBayesian Network

**Title: Bayesian Network Inference Program**

**Introduction:**
Bayesian networks, also known as belief networks or Bayes nets, are probabilistic graphical models that represent a set of variables and their probabilistic dependencies. These networks are extensively used in artificial intelligence and machine learning for modeling uncertain knowledge and making probabilistic inferences. The primary advantage of Bayesian networks lies in their ability to efficiently represent and update probabilistic beliefs in the face of new evidence.

**Objective:**
The objective of this practical is to implement a program that performs inference on a given Bayesian network. Inference, in the context of Bayesian networks, involves updating the probabilities of variables based on observed evidence. The program should be capable of incorporating new information and adjusting the beliefs about the variables accordingly.

**Key Concepts:**
1. **Bayesian Networks:**
   - A Bayesian network is a directed acyclic graph (DAG) where nodes represent random variables, and edges represent probabilistic dependencies between them.
   - Conditional Probability Tables (CPTs) are associated with each node, specifying the probability distribution of a variable given its parents.

2. **Inference in Bayesian Networks:**
   - Inference involves calculating the posterior probabilities of variables given observed evidence.
   - Two common methods for inference are:
     - **Exact Inference:** Utilizes methods like Variable Elimination or Belief Propagation to compute exact probabilities.
     - **Approximate Inference:** Employs sampling techniques like Markov Chain Monte Carlo (MCMC) for probabilistic estimation.

**Program Design:**
1. **Input:**
   - The program should take as input the structure of the Bayesian network, including nodes, edges, and CPTs.
   - User-provided evidence, indicating observed values for specific variables.

2. **Inference Algorithm:**
   - Implement an inference algorithm capable of updating probabilities based on evidence.
   - The choice of algorithm (exact or approximate) can be based on user preference or system requirements.

3. **Output:**
   - Display the posterior probabilities of variables after incorporating the provided evidence.
   - Optionally, visualize the updated probability distribution using graphs or tables.

**Implementation Considerations:**
1. **Data Structures:**
   - Efficiently represent the Bayesian network, potentially using adjacency lists or matrices for graph representation.
   - Develop data structures to store and update CPTs.

2. **Algorithm Selection:**
   - Choose an inference algorithm based on the size and complexity of the Bayesian network.
   - For larger networks, approximate methods might be more practical.

3. **User Interface:**
   - Design a user-friendly interface for inputting network structure and evidence.
   - Clearly present the results of the inference process.

**Conclusion:**
In conclusion, this practical aims to provide hands-on experience in implementing a Bayesian network inference program. Understanding the fundamental concepts of Bayesian networks and their application in probabilistic reasoning is crucial for students pursuing artificial intelligence. Through this exercise, students will gain practical insights into how these models can be employed to make informed decisions in uncertain environments.

**Variable Elimination in Bayesian Networks:**

Variable Elimination is a fundamental algorithm used in the inference process of Bayesian networks. Its primary purpose is to compute the marginal probabilities of variables in a network given observed evidence. This algorithm is particularly useful for exact inference in Bayesian networks, where the goal is to calculate the exact probabilities of variables based on the available information.

**Key Steps in Variable Elimination:**

1. **Initialization:**
   - Begin by initializing the factors for each variable in the Bayesian network. A factor is a function that represents the probability distribution of a variable given its parents in the network.

2. **Evidence Incorporation:**
   - Modify the factors based on the observed evidence. This involves setting the probabilities of variables to 1 or 0 based on the evidence provided.

3. **Variable Ordering:**
   - Choose an order in which variables will be eliminated. The order significantly impacts the efficiency of the algorithm. A good variable order minimizes the size of intermediate factors during elimination.

4. **Variable Elimination Loop:**
   - Iterate through the variables in the chosen order, eliminating them by multiplying and summing over factors.
   - For each variable, multiply the relevant factors and sum out the variable, resulting in a new factor.
   - Repeat this process until all variables are eliminated except for the query variable.

5. **Normalization:**
   - Normalize the final factor for the query variable to obtain the marginal probability distribution.

**Example:**

Consider a simple Bayesian network with three variables A, B, and C, where A and B are parents of C. The factors for this network might be represented as:

- Factor for A: P(A)
- Factor for B: P(B)
- Factor for C given A and B: P(C | A, B)

If we want to find P(C | evidence), where evidence is information about the value of some variables, Variable Elimination would involve manipulating these factors to obtain the desired probability.

**Advantages:**

1. **Exact Inference:**
   - Variable Elimination provides exact inference in Bayesian networks, ensuring that the calculated probabilities are precise.

2. **Efficiency:**
   - The choice of variable ordering can significantly improve the efficiency of the algorithm, making it practical for moderately-sized networks.

3. **Optimizations:**
   - Various optimizations, such as caching intermediate results, can further improve the algorithm's performance.

Variable Elimination is a foundational technique in Bayesian network inference and is widely used due to its ability to provide accurate results in a computationally efficient manner.

## Files

- [main.min.py](./main.min.py) - Minified without external comments
- [main.py](./main.py)
- [heart.csv](./heart.csv) - Place next to script
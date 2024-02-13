# P5_BayesianNetwork

## Title: Creating a Bayesian Network from Data

**Introduction:**
Bayesian Networks (BNs), also known as Bayesian Belief Networks or Bayesian Directed Acyclic Graphs (DAGs), are probabilistic graphical models that represent a set of random variables and their conditional dependencies via a directed acyclic graph. These networks are widely used in various fields, including Artificial Intelligence, as powerful tools for reasoning under uncertainty.

**Objective:**
The primary objective of this practical is to equip students with the knowledge and skills to construct a Bayesian Network from given data. This involves understanding the underlying probabilistic relationships between variables and utilizing this information to build a graphical model that accurately represents these dependencies.

**Theory:**

1. **Bayesian Networks Overview:**
   - A Bayesian Network consists of nodes and directed edges. Nodes represent random variables, and directed edges represent probabilistic dependencies.
   - The network structure is acyclic, preventing the occurrence of loops, ensuring a clear causal direction.

2. **Conditional Independence:**
   - Fundamental to Bayesian Networks is the concept of conditional independence. A node is conditionally independent of its non-descendants given its parents.
   - This property significantly reduces the number of parameters needed to specify the joint probability distribution of the variables.

3. **Nodes and Variables:**
   - Nodes in a Bayesian Network correspond to variables. These can be discrete or continuous, depending on the nature of the data.
   - Variables are classified into three types: observable (input), hidden (latent), and evidence (observed).

4. **Probabilistic Dependencies:**
   - The edges between nodes represent probabilistic dependencies. Each node is associated with a conditional probability distribution given its parents.
   - The joint probability distribution of all variables is the product of these conditional distributions.

5. **Parameterization:**
   - Parameters in a Bayesian Network are probabilities. Conditional Probability Tables (CPTs) specify the probability distribution of a node given its parents.
   - Learning these parameters from data is a crucial step in building a Bayesian Network.

**Steps in Constructing a Bayesian Network:**

1. **Identify Variables:**
   - Determine the variables in the domain and their relationships.

2. **Define Structure:**
   - Establish the structure of the network by identifying the dependencies between variables. This is often based on domain knowledge or statistical analysis.

3. **Parameterize the Network:**
   - Assign probabilities to the nodes based on the observed data. This involves constructing Conditional Probability Tables (CPTs).

4. **Verify and Refine:**
   - Validate the network against the data and refine as necessary. Bayesian Networks are iterative models that can be improved with additional information.

**Conclusion:**
Constructing a Bayesian Network from data is a valuable skill in the field of Artificial Intelligence. It allows for efficient representation of probabilistic relationships and facilitates reasoning under uncertainty. This practical aims to provide students with hands-on experience in building these networks, enhancing their understanding of probabilistic graphical models.

Dataset is available on <https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci>

## Files

- [main.py](./main.py)
- [heart.csv](./heart.csv) - Place next to script
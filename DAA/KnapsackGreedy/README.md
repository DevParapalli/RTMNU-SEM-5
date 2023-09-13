# Knapsack

The knapsack problem is the following problem in combinatorial optimization:

> Given a set of items, each with a weight and a value, determine which items to include in the collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

he most common problem being solved is the 0-1 knapsack problem, which restricts the number $ x_{i} $ of copies of each kind of item to zero or one. Given a set of $n$ items numbered from $1$ up to $n$, each with a weight $ w_{i} $ and a value $ v_{i} $, along with a maximum weight capacity $W$,

maximize $\sum _{i=1}^{n}v_{i}x_{i}$

subject to $\sum _{i=1}^{n}w_{i}x_{i}\leq W$ and $x_{i}\in \{0,1\}$.

Informally, the problem is to maximize the sum of the values of the items in the knapsack so that the sum of the weights is less than or equal to the knapsack's capacity.

George Dantzig proposed a greedy approximation algorithm to solve the unbounded knapsack problem. His version sorts the items in decreasing order of value per unit of weight,
${\displaystyle v_{1}/w_{1}\geq \cdots \geq v_{n}/w_{n}}.$ It then proceeds to insert them into the sack, starting with as many copies as possible of the first kind of item until there is no longer space in the sack for more. Provided that there is an unlimited supply of each kind of item, if $m$ is the maximum value of items that fit into the sack, then the greedy algorithm is guaranteed to achieve at least a value of $m/2$.

For the bounded problem, where the supply of each kind of item is limited, the above algorithm may be far from optimal. Nevertheless, a simple modification allows us to solve this case: Assume for simplicity that all items individually fit in the sack ($w_i \le W$ for all $i$). Construct a solution $S_1$ by packing items greedily as long as possible, i.e. ${S_1=\{1,\ldots,k\}}$ where ${k=\textstyle\max_{1\le k'\le n}\textstyle\sum_{i=1}^{k'} w_i\le W}$. Furthermore, construct a second solution $S_2=\{k+1\}$ containing the first item that did not fit. Since $S_1\cup S_2$ provides an upper bound for the Linear programming relaxation of the problem, one of the sets must have value at least $m/2$; we thus return whichever of $S_1$ and $S_2$ has better value to obtain a $1/2$-approximation.

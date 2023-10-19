# P9_ConstraintSatisfaction

- <https://www.ijcsmc.com/docs/papers/May2015/V4I5201520.pdf>

## Written

Constraint satisfaction problems (CSPs) are mathematical questions defined as a set of objects whose state must satisfy a number of constraints or limitations. CSPs represent the entities in a problem as a homogeneous collection of finite constraints over variables, which is solved by constraint satisfaction methods. CSPs are the subject of research in both artificial intelligence and operations research, since the regularity in their formulation provides a common basis to analyze and solve problems of many seemingly unrelated families. CSPs often exhibit high complexity, requiring a combination of heuristics and combinatorial search methods to be solved in a reasonable time.

Formally, a constraint satisfaction problem is defined as a triple $\langle X,D,C \rangle$, where

- $X = \{X_1, \ldots,X_n\}$ is a set of variables,
- $D = \{D_1, \ldots, D_n\}$ is a set of their respective domains of values, and
- $C = \{C_1, \ldots, C_m\}$ is a set of constraints.

Each variable $X_i$ can take on the values in the nonempty domain $D_i$.
Every constraint $C_j \in C$ is in turn a pair $\langle t_j,R_j \rangle$, where $t_j \subseteq X$ is a subset of $k$ variables and $R_j$ is a $k$-ary relation on the corresponding subset of domains $D_j$. An `evaluation` of the variables is a function from a subset of variables to a particular set of values in the corresponding subset of domains. An evaluation $v$ satisfies a constraint $\langle t_j, R_j \rangle$ if the values assigned to the variables $t_j$ satisfy the relation $R_j$.

An evaluation is `consistent` if it does not violate any of the constraints. An evaluation is `complete` if it includes all variables. An evaluation is a `solution` if it is consistent and complete; such an evaluation is said to `solve` the constraint satisfaction problem.

The 8-Queen Problem is a classic example of a Constraint Satisfaction Problem (CSP) in the field of artificial intelligence and computer science. In this problem, the task is to place eight queens on an 8x8 chessboard in such a way that no two queens threaten each other. The queens must be placed in a manner that no two queens share the same row, column, or diagonal.

In this case, variables are the position of the queens on the chessboard. Each variable represents the row in which a queen is places. ie, The Domain for each variable is ${\{0, 1, 2, 3, 4, 5, 6, 7\}}$

Constraints define that no two queens can threaten each other. ie.

- all(queen.row) = distinct
- all(queen.column) = distinct
- No two queen can share same diagonal.

To solve the 8-Queen problem, we utilize Backtracking, Constant Propagation and Heuristics.

In the context of the 8-Queen Problem, backtracking involves systematically tying out different assignments for the variables and backtracking when a conflict is encountered.

Constraint Propagation involves using the constraints of the problem to reduce the search space. In the 8-Queen Problem, this can be implemented by considering the constraints at each step and eliminating options that violate those constraints.

Heuristics are strategies used to guide the search process more efficiently.

---

One common heuristic is to prioritize the placement of queens in rows with fewer available options, aiming to detect conflicts earlier in the search process.

Various optimizations can be applied to improve the efficiency of the search. For example, symmetry-breaking techniques can be used to reduce redundant symmetrical solutions. Additionally, early detection of infeasible solution can prune parts of the search space, preventing the algorithm from exploring paths that lead to invalid configurations.

---

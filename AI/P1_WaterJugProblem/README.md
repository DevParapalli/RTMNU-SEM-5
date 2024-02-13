# Practical 1 : Water Jug Problem

The Water Jug Problem is a classic computational puzzle that involves two water jugs of different capacities and a target amount of water to be measured using these jugs. The goal is to find a sequence of jug fillings and pourings that will result in exactly the desired amount of water in one of the jugs or both.

## Problem Statement

```txt
You are given two empty jugs, Jug A and Jug B, with capacities 'a' and 'b' liters, respectively, 
where 'a' and 'b' are positive integers. There is also a target amount of water, 't' liters, 
that you need to measure using these two jugs. The following operations are allowed:

1. Fill Jug A to its maximum capacity.
2. Fill Jug B to its maximum capacity.
3. Pour water from Jug A into Jug B until Jug B is full or Jug A is empty.
4. Pour water from Jug B into Jug A until Jug A is full or Jug B is empty.
5. Empty the water from Jug A.
6. Empty the water from Jug B.

The problem is to determine if it is possible to measure exactly 't' liters of water using these operations, 
and if possible, then find the sequence of steps to achieve this goal.
```

To solve this problem, various algorithms and techniques can be employed, such as depth-first search (DFS), breadth-first search (BFS), or recursive approaches. The key is to keep track of the states of the two jugs during the process, avoid loops, and find a sequence that leads to the desired target amount. The accompanying program uses BFS with a Queue data structure.

## Files

- [main.min.py](./main.min.py) - Minified without external comments
- [main.py](./main.py)
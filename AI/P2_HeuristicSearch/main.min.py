#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Devansh Parapalli"

import math

C = {
    'A': (0, 0),
    'B': (18, 3),
    'C': (11, 24),
    'D': (7, 21),
    'E': (4, 18),
    'F': (1, 15),
    'G': (2, 12),
    'H': (5, 9),
}

def dist(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def dist_tbl(cities):
    distance_table = {}
    for city1 in cities:
        distance_table[city1] = {}
        for city2 in cities:
            distance_table[city1][city2] = round(dist(cities[city1], cities[city2]), 2)
    return distance_table

def prt_dist_tbl(distance_table):
    for c in distance_table:
        print(f"\t  {c}", end='')
    print()
    for c in distance_table:
        print(f"{c}", end='')
        for c2 in distance_table[c]:
            print(f"\t{distance_table[c][c2]:05.2f}", end='')
        print()
    print()

def tsp(dist):
    cur_c: str = 'A'
    V: list[str] = ['A']
    t_dist: float = 0.0
    while len(V) < len(dist):
        near_c: str = ''
        near_dist: float = math.inf
        for c in dist[cur_c]:
            if c not in V:
                if dist[cur_c][c] < near_dist:
                    near_c = c
                    near_dist = dist[cur_c][c]
        V.append(near_c)
        t_dist += near_dist
        cur_c = near_c
    t_dist += dist[V[-1]]['A']
    V.append('A')
    return round(t_dist, 2), V

if __name__ == "__main__":
    _dist_tbl = dist_tbl(C)
    prt_dist_tbl(_dist_tbl)
    t_dist, path = tsp(_dist_tbl)
    print(f"Total distance traveled: {t_dist} units")
    print(f"Path: {' -> '.join(path)}")
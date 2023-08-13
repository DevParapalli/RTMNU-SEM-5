#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Devansh Parapalli"

# Imports
from typing import Literal
import math

# Cities as their name, and grid positions
cities: dict[str, tuple[int, int]] = {
    'A': (0, 0),
    'B': (18, 3),
    'C': (11, 24),
    'D': (7, 21),
    'E': (4, 18),
    'F': (1, 15),
    'G': (2, 12),
    'H': (5, 9),
}


def calculate_distance(city1: tuple[int, int], city2: tuple[int, int]):
    """distance between two cities"""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def create_distance_table(cities: dict[str, tuple[int, int]]):
    """create a distance matrix for all cities"""
    distance_table: dict[str, dict[str, float]] = {}
    for city1 in cities:
        distance_table[city1] = {}
        for city2 in cities:
            distance_table[city1][city2] = round(calculate_distance(cities[city1], cities[city2]), 2)
    return distance_table

def print_distance_table(distance_table: dict[str, dict[str, float]]):
    """print the distance table"""
    for c in distance_table:
        print(f"\t  {c}", end='')
    print()
    for c in distance_table:
        print(f"{c}", end='')
        for c2 in distance_table[c]:
            print(f"\t{distance_table[c][c2]:05.2f}", end='')
        print()
    print()

def solve_tsp_nn(distances: dict[str, dict[str, float]]):
    """solve the TSP using Nearest Neighbour algorithm"""
    # Start at city A
    current_city: str = 'A'
    # List of cities visited
    visited: list[str] = ['A']
    # Total distance travelled
    total_distance: float = 0.0
    # Loop until all cities are visited
    while len(visited) < len(distances):
        # Get the nearest city
        nearest_city: str = ''
        nearest_distance: float = math.inf
        for city in distances[current_city]:
            if city not in visited:
                if distances[current_city][city] < nearest_distance:
                    nearest_city = city
                    nearest_distance = distances[current_city][city]
        # Add the nearest city to visited
        visited.append(nearest_city)
        # Add the distance to the total distance
        total_distance += nearest_distance
        # Set the current city to the nearest city
        current_city = nearest_city
    # Add the distance from the last city to the first city
    total_distance += distances[visited[-1]]['A']
    visited.append('A')
    # Return the total distance and the path
    return round(total_distance, 2), visited

if __name__ == "__main__":
    distance_table = create_distance_table(cities)
    print_distance_table(distance_table)
    total_distance, path = solve_tsp_nn(distance_table)
    print(f"Total distance travelled: {total_distance} units")
    print(f"Path: {' -> '.join(path)}")
    

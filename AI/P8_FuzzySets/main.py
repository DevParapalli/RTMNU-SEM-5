from __future__ import annotations

from functools import reduce
from typing import Type


class InvalidMembershipException(Exception):
    pass

class FuzzySet():
    values: set[tuple[str, float]]
    name: str
    domain: str
    def __init__(self, name, values:set[tuple[str, float]]|None=None, domain: str = 'U'):
        if values is None:
            values = set()
        self.name = name
        for (value, membership) in values:
            if (membership < 0 or membership > 1) or (not isinstance(value, (str, tuple))):
                raise InvalidMembershipException(f"{value} Membership must be in [0, 1]")
        self.values = values
        self.domain = domain
    
    def get_membership(self, value: str):
        for (val, membership) in self.values:
            if val == value:
                return membership
        return 0
    
    def __iter__(self):
        return iter(self.values)

    def __str__(self):
        return f"{self.name}: {self.values}"
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other: FuzzySet):
        return self.name == other.name and reduce(lambda x, y: x and y, map(lambda x: x in other.values, self.values), True)
    
    def __hash__(self):
        return hash(self.name)
    
    def __contains__(self, value: tuple[str, float]):
        return self.get_membership(value[0]) != 0
    
    def __len__(self):
        return len(self.values)
    
    def compliment(self):
        return FuzzySet(f"~{self.name}", set(map(lambda x: (x[0], 1 - x[1]), self.values)))
    
    def intersection(self, other: FuzzySet):
        new_values = set()
        for (value, membership) in self.values:
            if other.get_membership(value) != 0:
                new_values.add((value, min(membership, other.get_membership(value))))
        return FuzzySet(f"{self.name} ∩ {other.name}", new_values)
    
    def union(self, other: FuzzySet):
        new_values = set()
        for (value, membership) in self.values:
                new_values.add((value, max(membership, other.get_membership(value))))
        for (value, membership) in other.values:
            if self.get_membership(value) == 0:
                new_values.add((value, membership))
        return FuzzySet(f"{self.name} U {other.name}", new_values)
    
    def __mul__(self, other: FuzzySet | int | float):
        if isinstance(other, FuzzySet):
            if self.domain != other.domain:
                return self.cartesian_product(other)
            else:
                new_values = set()
                for (value, membership) in self.values:
                    if (value, membership) in other:
                        new_values.add((value, membership * other.get_membership(value)))
                return FuzzySet(f"{self.name} x {other.name}", new_values)
        elif isinstance(other, (int, float)):
            return self.crisp_product(other)
    
    def crisp_product(self, d: float | int):
        new_values = set()
        for (value, membership) in self.values:
            new_values.add((value, membership * d))
        return FuzzySet(f"{self.name} x {d}", new_values)
    
    def __pow__(self, d: float | int):
        new_values = set()
        for (value, membership) in self.values:
            new_values.add((value, membership ** d))
        return FuzzySet(f"{self.name}^{d}", new_values)
    
    def power(self, d: float | int):
        return self.__pow__(d)
    
    def __add__(self, other: FuzzySet):
        new_values = set()
        for (value, membership) in self.values:
            _m = membership + other.get_membership(value) - (membership * other.get_membership(value))
            new_values.add((value, _m))
        for (value, membership) in other.values:
            if self.get_membership(value) == 0:
                new_values.add((value, membership))
        return FuzzySet(f"{self.name} + {other.name}", new_values)
    
    def add(self, other: tuple[str, float]):
        self.values.add(other)
    
    def bounded_sum(self, other):
        new_values = set()
        for (value, membership) in self.values:
            if (value, membership) in other:
                _m = min(1, membership + other.get_membership(value))
                new_values.add((value, _m))
            else:
                new_values.add((value, membership))
        return FuzzySet(f"{self.name} ⊕ {other.name}", new_values)
    
    def __sub__(self, other: FuzzySet):
        new_values = set()
        for (value, membership) in self.values:
            if (value, membership) in other:
                new_values.add((value, min(membership, 1 - other.get_membership(value))))
            else:
                new_values.add((value, membership))
        return FuzzySet(f"{self.name} - {other.name}", new_values)
    
    def sub(self, other: FuzzySet):
        return self.__sub__(other)
    
    def bounded_sub(self, other: FuzzySet):
        new_values = set()
        for (value, membership) in self.values:
            if (value, membership) in other:
                _m = max(0, membership + other.get_membership(value) - 1)
                new_values.add((value, _m))
            else:
                new_values.add((value, membership))
        return FuzzySet(f"{self.name} ⊖ {other.name}", new_values)

    def cartesian_product(self, other: FuzzySet):
        new_values = set()
        for (value, membership) in self.values:
            for (value2, membership2) in other:
                new_values.add(((value, value2), min(membership, membership2)))
        return FuzzySet(f"{self.name} xᶜ {other.name}", new_values)
    


def main():
    A = FuzzySet("A", {("P", 0.9), ("Q", 0.1)})
    B = FuzzySet("B", {("P", 0.8), ("Q", 0.2)})
    C = FuzzySet("C", {("S", 0.7), ("T", 0.3)}, "V")
    
    print(A.intersection(B))
    print(A.union(B))
    print(A.compliment())
    print(A * B)
    print(A + B)
    print(A - B)
    # Cartesian product
    X = A * C
    Y = C * A
    print(X)
    print(Y)
    print(X == Y)

if __name__ == "__main__":
    main()
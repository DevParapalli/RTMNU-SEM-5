#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Devansh Parapalli"

from math import sqrt as s, inf as i

p = print
r = round
l = len

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

def d(c, c2):
    return s((c[0] - c2[0])**2 + (c[1] - c2[1])**2)

def cdt(c):
    dt = {}
    for c1 in c:
        dt[c1] = {}
        for c2 in c:
            dt[c1][c2] = r(d(c[c1], c[c2]), 2)
    return dt

def pdt(dt):
    for c in dt:
        p(f"\t  {c}", end='')
    p()
    for c in dt:
        p(f"{c}", end='')
        for c2 in dt[c]:
            p(f"\t{dt[c][c2]:05.2f}", end='')
        p()
    p()

def t(d):
    cc = 'A'
    v = ['A']
    td = 0.0
    while l(v) < l(d):
        nc = ''
        nd = i
        for c in d[cc]:
            if c not in v and d[cc][c] < nd:
                nc = c
                nd = d[cc][c]
        v.append(nc)
        td += nd
        cc = nc
    td += d[v[-1]]['A']
    v.append('A')
    return r(td, 2), v

if __name__ == "__main__":
    dt = cdt(C)
    pdt(dt)
    td, _p = t(dt)
    p(f"Total distance traveled: {td} units")
    p(f"Path: {' -> '.join(_p)}")
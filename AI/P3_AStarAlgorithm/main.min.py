from collections import deque

class Graph:
    def __init__(self, am):
        self.am = am
        self._H = {}
        for n in self.am:
            for (m, w) in self.am[n]:
                self._H[m] = 1
    def gn(self, v):
        return self.am[v]
    def h(self, n):
        return self._H[n]
    def a_star(self, S, G):
        OL = set([S])
        CL = set([])
        g = {}
        g[S] = 0
        P = {}
        P[S] = S
        while len(OL) > 0:
            n = None
            for v in OL:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v
            if n == None:
                print('NO PATH EXISTS')
                return None
            if n == G:
                rp = []
                while P[n] != n:
                    rp.append(n)
                    n = P[n]
                rp.append(S)
                rp.reverse()
                print('Path found: {}'.format(rp))
                return rp
            for (m, w) in self.gn(n):
                if m not in OL and m not in CL:
                    OL.add(m)
                    P[m] = n
                    g[m] = g[n] + w
                else:
                    if g[m] > g[n] + w:
                        g[m] = g[n] + w
                        P[m] = n
                        if m in CL:
                            CL.remove(m)
                            OL.add(m)
            OL.remove(n)
            CL.add(n)
        print('NO PATH EXISTS')
        return None

if __name__ == "__main__":
    AM = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 1)]
    }
    G = Graph(AM)
    G.a_star('A', 'D')
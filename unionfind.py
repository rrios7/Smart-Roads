class UnionFind:
    def __init__(self, size):
        self.disjoint_set = [i for i in range(size)]

    def find(self, u, v):
        return self.disjoint_set[u] == self.disjoint_set[v]

    def union(self, u, v):
        aux = self.disjoint_set[u]

        for i in range(len(self.disjoint_set)):
            if self.disjoint_set[i] == aux:
                self.disjoint_set[i] = self.disjoint_set[v]
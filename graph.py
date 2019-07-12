from queue import PriorityQueue
from unionfind import UnionFind


class Edge:
    def __init__(self, origin, dest, weight):
        self.origin = origin
        self.dest = dest
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'{self.origin} -> {self.dest} : {self.weight}'


class Vertex:
    def __init__(self, index):
        self.index = index
        self.edges = list()


class Graph:
    def __init__(self):
        self.vertexes = dict()
        self.size = 0
        self.edges = list()

    def empty(self):
        return self.size == 0

    def add_vertex(self, label):
        if label in self.vertexes:
            return

        self.vertexes[label] = Vertex(self.size)
        self.size += 1

    def remove_vertex(self, label):
        if label not in self.vertexes:
            return

        flag = False

        for vertex in self.vertexes.values():
            if flag:
                vertex.index -= 1

            if vertex.index == self.vertexes[label].index:
                flag = True

            for edge in vertex.edges:
                if edge.origin == label or edge.dest == label:
                    vertex.edges.remove(edge)

        self.vertexes.pop(label)
        self.size -= 1

    def add_edge(self, origin, dest, weight=1, directed=False):
        if origin not in self.vertexes and dest not in self.vertexes:
            return

        self.vertexes[origin].edges.append(Edge(origin, dest, weight))

        if not directed:
            self.vertexes[dest].edges.append(Edge(dest, origin, weight))

        self.edges.append(Edge(origin, dest, weight))

    def remove_edge(self, origin, dest, directed=False):
        if origin not in self.vertexes and dest not in self.vertexes:
            return

        for edge in self.vertexes[origin].edges:
            if edge.dest == dest:
                self.vertexes[origin].edges.remove(edge)

        if not directed:
            for edge in self.vertexes[dest].edges:
                if edge.dest == origin:
                    self.vertexes[dest].edges.remove(edge)

    def bfs(self, origin):
        if self.empty() or origin not in self.vertexes:
            return

        queue = list()
        visited = list()

        queue.append(origin)

        while len(queue) > 0:
            current_vertex = queue.pop(0)

            if current_vertex in visited:
                continue

            visited.append(current_vertex)

            for edge in self.vertexes[current_vertex].edges:
                if edge.dest not in visited:
                    queue.append(edge.dest)

        return visited

    def dfs(self, origin):
        if self.empty() or origin not in self.vertexes:
            return

        stack = list()
        visited = list()

        stack.insert(0, origin)

        while len(stack) > 0:
            current_vertex = stack.pop(0)

            if current_vertex in visited:
                continue

            visited.append(current_vertex)

            for edge in self.vertexes[current_vertex].edges:
                if edge.dest not in visited:
                    stack.insert(0, edge.dest)

        return visited

    def enqueue_edges(self, vertex, queue):
        for edge in vertex.edges:
            queue.put(edge)

    def kruskal(self):
        queue = PriorityQueue()
        mst = list()
        mst_weight = 0
        uf = UnionFind(len(self.vertexes))

        for edge in self.edges:
            queue.put(edge)

        while not queue.empty() and len(mst) < self.size:
            current_edge = queue.get()

            if not uf.find(self.vertexes[current_edge.origin].index, self.vertexes[current_edge.dest].index):
                uf.union(self.vertexes[current_edge.origin].index, self.vertexes[current_edge.dest].index)
                mst.append(current_edge)
                mst_weight += current_edge.weight

        return mst, mst_weight

    def prim(self, origin):
        queue = PriorityQueue()
        visited = list()
        mst = list()
        mst_weight = 0

        visited.append(origin)
        self.enqueue_edges(self.vertexes[origin], queue)

        while not queue.empty() and len(mst) < self.size:
            current_edge = queue.get()
            if current_edge.dest in visited:
                continue

            visited.append(current_edge.dest)
            mst.append(current_edge)
            mst_weight += current_edge.weight

            self.enqueue_edges(self.vertexes[current_edge.dest], queue)

        return mst, mst_weight

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        res = ''

        for label, vertex in self.vertexes.items():
            res += f'{label} ->'
            for edge in vertex.edges:
                res += f' {edge.dest}:{edge.weight}'
            res += '\n'

        return res

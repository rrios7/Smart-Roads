import math
from queue import PriorityQueue
from unionfind import UnionFind


class Edge:
    def __init__(self, origin, dest, distance, speed, capacity):
        self.origin = origin
        self.dest = dest
        self.distance = distance
        self.heuristic = 0 
        self.speed = speed
        self.time = (self.distance / speed) * 60
        self.weight = self.time
        self.capacity = capacity
        self.current_flow = 0
    
    def update(self, value):
        self.current_flow += value

        if self.current_flow > self.capacity:
            self.weight = (self.time + ((self.current_flow - self.capacity) / self.capacity)) * self.time
        else:
            self.weight = self.time

    def __lt__(self, other):
        if self.heuristic == 0:
            return self.weight < other.weight

        return self.heuristic < other.heuristic

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'{self.origin} -> {self.dest} : {self.weight} : {self.heuristic}'


class Vertex:
    def __init__(self, index, x, y):
        self.index = index
        self.x_coord = x
        self.y_coord = y
        self.edges = list()
        self.map = dict()

    def __sub__(self, other):
        return (self.x_coord - other.x_coord) ** 2 + (self.y_coord - other.y_coord) ** 2


class Graph:
    def __init__(self):
        self.vertexes = dict()
        self.size = 0
        self.edges = list()
        self.important_vertexes = list()

    def empty(self):
        return self.size == 0

    def add_vertex(self, label, x=None, y=None, important=False):
        if label in self.vertexes:
            return

        self.vertexes[label] = Vertex(self.size, x, y)
        self.size += 1
        
        if important:
            self.important_vertexes.append(label)

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

    def add_edge(self, origin, dest, speed, capacity, directed=False):
        if origin not in self.vertexes and dest not in self.vertexes:
            return

        distance =  math.sqrt(self.vertexes[origin] - self.vertexes[dest])

        self.vertexes[origin].edges.append(Edge(origin, dest, distance, speed, capacity))
        
        if not directed:
            self.vertexes[dest].edges.append(Edge(dest, origin, distance, speed, capacity))

        self.edges.append(Edge(origin, dest, distance, speed, capacity))

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

    def prim_helper(self, vertex, queue):
        for edge in vertex.edges:
            queue.put(edge)

    def prim(self, origin):
        queue = PriorityQueue()
        visited = list()
        mst = list()
        mst_weight = 0

        visited.append(origin)
        self.prim_helper(self.vertexes[origin], queue)

        while not queue.empty() and len(mst) < self.size:
            current_edge = queue.get()
            if current_edge.dest in visited:
                continue

            visited.append(current_edge.dest)
            mst.append(current_edge)
            mst_weight += current_edge.weight

            self.prim_helper(self.vertexes[current_edge.dest], queue)

        return mst, mst_weight

    def shortest_path(self, origin, dest, algorithm):
        vertex_data = dict()

        for vertex in self.vertexes:
            vertex_data[vertex] = (math.inf, '')

        if not algorithm(origin, dest, vertex_data):
            return 0, 'No hay camino'

        path = list()
        aux = dest

        while aux != origin:
            path.append(aux)
            aux = vertex_data[aux][1]

        path.append(origin)
        path.reverse()

        return path, vertex_data[dest][0]

    def enqueue_edges(self, current_vertex, visited, vertex_data, queue, dest=None):
        for edge in self.vertexes[current_vertex].edges:
            if edge.dest not in visited:
                aux = vertex_data[current_vertex][0] + edge.weight

                if aux < vertex_data[edge.dest][0]:
                    vertex_data[edge.dest] = (aux, current_vertex)

                    if dest is not None:
                        edge.heuristic = self.heuristic(aux, edge.dest, dest)

                    queue.put(edge)

    def djikstra(self, origin, dest, vertex_data):
        queue = PriorityQueue()
        visited = list()

        current_vertex = origin
        vertex_data[origin] = (0, origin)
        visited.append(origin)
        self.enqueue_edges(current_vertex, visited, vertex_data, queue)

        while not queue.empty():
            current_vertex = queue.get().dest
            if current_vertex == dest:
                return True

            visited.append(current_vertex)
            self.enqueue_edges(current_vertex, visited, vertex_data, queue)

        return False

    def heuristic(self, weight, current_vertex, dest):
        return weight + math.sqrt(self.vertexes[current_vertex] - self.vertexes[dest])

    def a_star(self, origin, dest, vertex_data):
        found_path = False
        queue = PriorityQueue()
        visited = list()

        current_vertex = origin
        vertex_data[origin] = (0, origin)
        visited.append(origin)
        self.enqueue_edges(current_vertex, visited, vertex_data, queue, dest)

        while not queue.empty():
            current_edge = queue.get()

            current_edge.heuristic = 0

            if found_path:
                continue

            current_vertex = current_edge.dest

            if current_vertex == dest:
                found_path = True

            visited.append(current_vertex)

            self.enqueue_edges(current_vertex, visited, vertex_data, queue, dest)

        return found_path
    
    def all_pairs_shortest_path(self):
        for label, vertex in self.vertexes.items():
            for important_vertex in self.important_vertexes:
                
                if label == important_vertex:
                    continue
                    
                vertex.map[important_vertex] = (self.shortest_path(label, important_vertex, self.a_star))

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

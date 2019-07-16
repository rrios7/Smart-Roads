from graph import Graph

g = Graph()

g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')

g.add_edge('A', 'B', 7)
g.add_edge('B', 'C', 21)
g.add_edge('C', 'A', 8)
g.add_edge('C', 'E', 3)
g.add_edge('D', 'B', 5)
g.add_edge('E', 'D', 15)

print(f'El recorrido de anchura fue: {g.bfs("A")}')
print(f'El recorrido de profundiad fue: {g.dfs("A")}')

print(g)

tree, cost = g.kruskal()

print(f'El arbol de expansion minimo de Kruskal es {tree} y su costo es {cost}')

tree2, cost2 = g.prim('A')

print(f'El arbol de expansion minimo de Prim es {tree2} y su costo es {cost2}')

path, cost = g.shortest_path('A', 'D', g.djikstra)

print(f'El camino mas corto entre el par de vertices cuesta {cost} y se compone de {path}')

# A-Star Code :D!
# g = Graph()
#
# g.add_vertex('A', 2, 10)
# g.add_vertex('B', 5, 8)
# g.add_vertex('C', 11, 11)
# g.add_vertex('D', 2, 6)
# g.add_vertex('E', 12, 2)
# g.add_vertex('F', 4, 4)
# g.add_vertex('G', 8, 4)
# g.add_vertex('H', 6, 6)
# g.add_vertex('I', 12, 7)
# g.add_vertex('J', 15, 7)
# g.add_vertex('K', 14, 5)
# g.add_vertex('L', 14, 9)
# g.add_vertex('M', 5, 12)
#
#
# g.add_edge('A', 'B', 3)
# g.add_edge('A', 'D', 4)
# g.add_edge('A', 'M', 2)
# g.add_edge('B', 'D', 4)
# g.add_edge('B', 'H', 1)
# g.add_edge('B', 'M', 2)
# g.add_edge('C', 'L', 2)
# g.add_edge('C', 'M', 2)
# g.add_edge('D', 'F', 5)
# g.add_edge('E', 'G', 2)
# g.add_edge('E', 'K', 5)
# g.add_edge('F', 'H', 3)
# g.add_edge('G', 'H', 2)
# g.add_edge('I', 'K', 4)
# g.add_edge('I', 'L', 4)
# g.add_edge('J', 'K', 4)
# g.add_edge('J', 'L', 4)
#
# path, cost = g.shortest_path('M', 'E', g.a_star)
#
# print(f'El camino mas corto entre el par de vertices cuesta {cost} y se compone de {path}')


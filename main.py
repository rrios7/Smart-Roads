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
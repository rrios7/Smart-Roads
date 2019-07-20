from graph import Graph



# A-Star Code :D!
g = Graph()

g.add_vertex('A', 2, 10)
g.add_vertex('B', 5, 8)
g.add_vertex('C', 11, 11, True)
g.add_vertex('D', 2, 6)
g.add_vertex('E', 12, 2, True)
g.add_vertex('F', 4, 4)
g.add_vertex('G', 8, 4)
g.add_vertex('H', 6, 6)
g.add_vertex('I', 12, 7)
g.add_vertex('J', 15, 7, True)
g.add_vertex('K', 14, 5)
g.add_vertex('L', 14, 9)
g.add_vertex('M', 5, 12, True)


g.add_edge('A', 'B', 100, 100)
g.add_edge('A', 'D', 70, 843)
g.add_edge('A', 'M', 80, 24)
g.add_edge('B', 'D', 78, 175)
g.add_edge('B', 'H', 35, 210)
g.add_edge('B', 'M', 94, 120)
g.add_edge('C', 'L', 50, 210)
g.add_edge('C', 'M', 200, 444)
g.add_edge('D', 'F', 50, 1010)
g.add_edge('E', 'G', 20, 444)
g.add_edge('E', 'K', 50, 1010)
g.add_edge('F', 'H', 30, 666)
g.add_edge('G', 'H', 20, 444)
g.add_edge('I', 'K', 40, 888)
g.add_edge('I', 'L', 40, 888)
g.add_edge('J', 'K', 40, 888)
g.add_edge('J', 'L', 40, 888)

g.all_pairs_shortest_path()

print(g.vertexes['M'].map)
print(g.vertexes['A'].map)
print(g.vertexes['L'].map)
print(g.vertexes['K'].map)
print(g.vertexes['F'].map)
print(g.vertexes['H'].map)

 


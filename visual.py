import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from graph import Graph

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


g.add_edge('A', 'B', 100, 5)
g.add_edge('A', 'D', 70, 5)
g.add_edge('A', 'M', 80, 5)
g.add_edge('B', 'D', 78, 3)
g.add_edge('B', 'H', 35, 2)
g.add_edge('B', 'M', 94, 5)
g.add_edge('C', 'L', 50, 5)
g.add_edge('C', 'M', 200, 4)
g.add_edge('D', 'F', 50, 3)
g.add_edge('E', 'G', 20, 4)
g.add_edge('E', 'K', 50, 5)
g.add_edge('F', 'H', 30, 2)
g.add_edge('G', 'H', 20, 1)
g.add_edge('I', 'K', 40, 3)
g.add_edge('I', 'L', 40, 5)
g.add_edge('J', 'K', 40, 2)
g.add_edge('J', 'L', 40, 4)


def update_traffic():
    data = open('vehicles.txt', 'r').read()
    lines = data.split('\n')

    for line in lines:
        origin, dest, value = line.split(',')
        for edge in g.vertexes[origin].edges:
            if edge.dest == dest:
                edge.update(int(value))

    g.all_pairs_shortest_path()

    plot_routes()

    for vertex in g.vertexes.values():
        for edge in vertex.edges:
            edge.current_flow = 0

def plot_routes():
    for l, v in g.vertexes.items():
        plt.axis([0, 20, 0, 20])
        plt.title(f'Rutas de {l}')
        plt.xlabel('Eje de las abscisas')
        plt.ylabel('Eje de las ordenadas')
        purple_patch = mpatches.Patch(color='darkorchid', label='Ruta más rápida')
        plt.legend(handles=[purple_patch])
        for label, vertex in g.vertexes.items():
            if label in g.important_vertexes:
                plt.plot(vertex.x_coord, vertex.y_coord, 'ro')
            else:
                plt.plot(vertex.x_coord, vertex.y_coord, 'bo')
            plt.annotate(label, xy=(vertex.x_coord, vertex.y_coord), xytext=(vertex.x_coord, vertex.y_coord + .5))
            for edge in vertex.edges:
                origin = g.vertexes[edge.origin]
                dest = g.vertexes[edge.dest]

                if edge.current_flow < edge.capacity:
                    color = 'green'
                elif edge.current_flow <= edge.capacity + 0.25 * edge.capacity:
                    color = 'gold'
                else:
                    color = 'red'

                plt.plot([origin.x_coord, dest.x_coord],
                         [origin.y_coord, dest.y_coord], color=color)

        for p in v.map.values():
            for i in range(len(p[0]) - 1):
                origin = g.vertexes[p[0][i]]
                dest = g.vertexes[p[0][i + 1]]
                plt.plot([origin.x_coord, dest.x_coord],
                         [origin.y_coord, dest.y_coord], 'darkorchid')
        plt.show()


while True:
    x = input('Presione x para salir')

    if x == 'x':
        break

    update_traffic()
    print(g)

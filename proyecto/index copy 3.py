import osmium
import networkx as nx

class OSMHandler(osmium.SimpleHandler):
    def __init__(self, graph):
        super(OSMHandler, self).__init__()
        self.graph = graph

    def node(self, n):
        # Agregar nodos al grafo
        self.graph.add_node(n.id, lon=n.location.lon, lat=n.location.lat)

    def way(self, w):
        # Agregar aristas al grafo
        nodes = w.nodes
        for i in range(1, len(nodes)):
            # Obtener los atributos del camino (way)
            weight = 1.0
            for tag in w.tags:
                if tag.k == "weight":
                    weight = float(tag.v)
                    break

            # Agregar arista dirigida y ponderada al grafo
            self.graph.add_edge(nodes[i - 1].ref, nodes[i].ref, weight=weight)

# Crear el grafo
graph = nx.DiGraph()

# Crear el manejador de OSM y aplicarlo al archivo OSM
osm_handler = OSMHandler(graph)
osm_handler.apply_file("map.osm")

ss = list(graph.nodes())

start_node = ss[0]
end_node = ss[100]

shortest_path = nx.dijkstra_path(graph, start_node, end_node , weight='weight')


print(shortest_path)

# for node in graph.nodes:
#     lon = graph.nodes[node]['lon']
#     lat = graph.nodes[node]['lat']
#     print(f"Longitud del nodo {node}: {lon}")
#     print(f"atitud del nodo {node}: {lat}")
    
# for u, v, attrs in graph.edges(data=True):
#     weight = attrs['weight']
#     print(f'Peso de la arista ({u}, {v}): {weight}')



# --------------------------------------------------------------------------------------------


# def encontrar_ruta_mas_corta(grafo, id_entrada, id_salida):
#     try:
#         ruta_mas_corta = nx.shortest_path(grafo, id_entrada, id_salida)
#         distancia = nx.shortest_path_length(grafo, id_entrada, id_salida)
#         return ruta_mas_corta, distancia
#     except nx.NetworkXNoPath:
#         return None, None

# # Ejemplo de uso
# grafo = nx.Graph()


# # Agregar nodos al grafo
# grafo.add_node("A")
# grafo.add_node("B")
# grafo.add_node("C")
# grafo.add_node("D")

# # Agregar aristas al grafo
# grafo.add_edge("A", "B", weight=4)
# grafo.add_edge("A", "C", weight=2)
# grafo.add_edge("B", "C", weight=1)
# grafo.add_edge("B", "D", weight=5)
# grafo.add_edge("C", "D", weight=8)

# id_entrada = "A"
# id_salida = "D"

# ruta, distancia = encontrar_ruta_mas_corta(grafo, id_entrada, id_salida)

# print(grafo.order())

# # if ruta is not None:
# #     print(f"La ruta más corta desde {id_entrada} hasta {id_salida} es: {ruta}")
# #     print(f"Distancia total: {distancia}")
# # else:
# #     print(f"No hay ruta disponible desde {id_entrada} hasta {id_salida}")



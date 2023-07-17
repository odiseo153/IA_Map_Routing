import osmium
import networkx as nx
import matplotlib.pyplot as plt

class OSMHandler(osmium.SimpleHandler):
    def __init__(self, graph):
        super(OSMHandler, self).__init__()
        self.graph = graph

    def node(self, n):
        # Agregar nodos al grafo con coordenadas geográficas
        self.graph.add_node(n.id, lon=n.location.lon, lat=n.location.lat)

    def way(self, w):
        # Agregar aristas al grafo
        nodes = w.nodes
        for i in range(1, len(nodes)):
            self.graph.add_edge(nodes[i - 1].ref, nodes[i].ref)

# Crear el grafo
graph = nx.Graph()

# Crear el manejador de OSM y aplicarlo al archivo OSM
osm_handler = OSMHandler(graph)
osm_handler.apply_file("santo_domingo.osm")

# Obtener las posiciones geográficas de los nodos
node_positions = {node_id: (data['lon'], data['lat']) for node_id, data in graph.nodes(data=True)}

# Visualizar el grafo manteniendo las posiciones geográficas
plt.figure(figsize=(10, 10))
nx.draw(graph, node_positions, node_size=10, node_color='blue', alpha=0.6, with_labels=False)
plt.show()

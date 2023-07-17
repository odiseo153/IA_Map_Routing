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
            self.graph.add_edge(nodes[i - 1].ref, nodes[i].ref)

# Crear el grafo
graph = nx.Graph()

# Crear el manejador de OSM y aplicarlo al archivo OSM
osm_handler = OSMHandler(graph)
osm_handler.apply_file("santo_domingo.osm")

# Ahora puedes utilizar el grafo para realizar cualquier operación que desees
# Por ejemplo, puedes obtener información sobre los nodos y aristas:
print("Número de nodos:", graph.number_of_nodes())
print("Número de aristas:", graph.number_of_edges())



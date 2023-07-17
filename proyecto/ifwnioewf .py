import osmium
import heapq
import networkx as nx
import heapq
import networkx as nx

def dijkstra_path(graph, start_node, end_node, weight='weight'):
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start_node] = 0

    # Usar una cola de prioridad para seleccionar el nodo con la distancia mínima en cada iteración
    queue = [(0, start_node)]
    visited = set()

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Ignorar nodos ya visitados
        if current_node in visited:
            continue

        # Marcar el nodo actual como visitado
        visited.add(current_node)

        # Si se alcanza el nodo de destino, se ha encontrado la ruta más corta
        if current_node == end_node:
            break

        # Explorar los vecinos del nodo actual
        for neighbor in graph.neighbors(current_node):
            weight_value = graph.edges[current_node, neighbor].get(weight, 1)
            distance = current_distance + weight_value

            # Si se encuentra una distancia más corta, actualizarla y agregar el vecino a la cola
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    if distances[end_node] == float('inf'):
        raise nx.NetworkXNoPath(f"No hay ruta entre {start_node} y {end_node}")

    # Reconstruir la ruta más corta
    path = [end_node]
    current = end_node
    total_distance = distances[end_node]

    while current != start_node:
        candidates = [(distances[neighbor], neighbor) for neighbor in graph.predecessors(current)]
        _, current = min(candidates)
        path.append(current)

    return list(reversed(path)), total_distance





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

start_node = 1268223834
end_node = 360429330

shortest_path = dijkstra_path(graph, start_node, end_node , weight='weight')


print(shortest_path)


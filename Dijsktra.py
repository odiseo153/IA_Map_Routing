import osmium
import networkx as nx
import heapq
from importar_osm import *




def ruta_dijkstra(graph, start_node, end_node, weight='weight'):
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





# start_node = 3246094326
# end_node = 1268224094

# shortest_path =  nx.dijkstra_path(graph, start_node, end_node , weight='weight')


# print(shortest_path)


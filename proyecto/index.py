import osmnx as ox
import networkx as nx

place_name = "santo domingo, dominican republic"
graph = ox.graph_from_place(place_name, network_type="drive")


fig, ax = ox.plot_graph_folium(graph, node_color="r")

# ox.plot_graph_folium(graph, popup_attribute='name',
#                      color='red', weight=2, opacity=0.7)

ox.save_graph_geopackage(graph, filepath="cordoba_net.gpkg")



orig = ox.distance.nearest_nodes(graph, X=18.473796432768566, Y=69.94138108025535)
dest = ox.distance.nearest_nodes(graph, X=-18.4599, Y=-69.9447)

route = ox.shortest_path(graph, orig, dest, weight="length")
fig, ax = ox.plot_graph_route(graph, route, node_size=0)


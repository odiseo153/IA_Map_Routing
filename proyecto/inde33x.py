import folium
from folium import plugins

# Crear el mapa inicial
mapa = folium.Map(location=[40.7128, -74.0060], zoom_start=13)

# Crear la lista de coordenadas de la ruta
ruta = [[40.7128, -74.0060], [40.7423, -74.0370], [40.7489, -73.9680], [40.6892, -74.0445]]

# Trazar la ruta en el mapa
folium.plugins.AntPath(locations=ruta).add_to(mapa)

# Guardar el mapa resultante en un archivo HTML
mapa.save("mapa.html")

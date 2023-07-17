import osmnx as ox
from gmplot import GoogleMapPlotter
import decimal

def crear_mapa(latitudes, longitudes, ruta_latitudes, ruta_longitudes, api_key):
    # Descargar los datos de OSM para las vías cercanas a las coordenadas
    graph = ox.graph_from_address("Santo Domingo , República Dominicana", network_type='all')

    # Obtener las coordenadas de las vía

    # Crear el mapa utilizando gmplot
    gmap = GoogleMapPlotter(latitudes[0], longitudes[0], 13, apikey=api_key)

    # Agregar las coordenadas de las vías al mapa
    edges = ox.graph_to_gdfs(graph, nodes=False, edges=True)
    for _, edge in edges.iterrows():
        gmap.plot(edge["geometry"].xy[1], edge["geometry"].xy[0], color='yellow', edge_width=1)

    # Agregar los marcadores de punto de inicio y destino al mapa
    gmap.scatter(latitudes, longitudes, color='red', size=40, marker=False)

    # Agregar la ruta al mapa
    gmap.plot(ruta_latitudes, ruta_longitudes, color='blue', edge_width=3)

    # Guardar el mapa en un archivo HTML
    gmap.draw("mapa2.html")

# Ejemplo de uso
if _name_ == '_main_':
    
    inicio = input('escriba el inicio').split(',')
    destino = input('escriba el destino').split(',')    
    
    

    # Coordenadas de ejemplo del punto de inicio y destino en Santo Domingo
    latitudes = [decimal.Decimal(inicio[0]), decimal.Decimal(destino[0])]  # Latitudes del punto de inicio y destino
    longitudes = [decimal.Decimal(inicio[1]), decimal.Decimal(destino[1])]  # Longitudes del punto de inicio y destino

    ruta_latitudes = [decimal.Decimal(inicio[0]), decimal.Decimal(destino[0])]  # Latitudes de la ruta
    ruta_longitudes = [decimal.Decimal(inicio[1]), decimal.Decimal(destino[1])]  # Longitudes de la ruta

    api_key = 'AIzaSyAsNkw2unLipVcy7FSIOwUcQGQDKMwqU6w'  # Reemplaza con tu propia clave de API de Google Maps

    crear_mapa(latitudes, longitudes, ruta_latitudes, ruta_longitudes,api_key)
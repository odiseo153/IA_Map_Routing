import folium
from folium import plugins
import webbrowser

def exportar(ruta):
    # Crear el mapa inicial
    mapa = folium.Map(location=[18.4009689, -70.13908], zoom_start=13)

    # Agregar marcadores para la entrada y la salida del trayecto
    folium.Marker(location=ruta[0], icon=folium.Icon(color='green')).add_to(mapa)  # Marcador de entrada (color verde)
    folium.Marker(location=ruta[-1], icon=folium.Icon(color='red')).add_to(mapa)  # Marcador de salida (color rojo)

    # Trazar la línea de trayecto en el mapa (color rojo)
    folium.PolyLine(locations=ruta, color='red').add_to(mapa)

    # Guardar el mapa resultante en un archivo HTML
    mapa.save("mapa.html")

    # Abrir el archivo HTML en el navegador predeterminado
    webbrowser.open("mapa.html")

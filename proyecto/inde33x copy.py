import tkinter as tk
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

class MapaInteractivo(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Mapa interactivo")
        self.master.geometry("800x600")
        self.create_map()

    def create_map(self):
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

        ax.coastlines()
        ax.stock_img()
        ax.set_global()

        plt.show()

ventana = tk.Tk()
app = MapaInteractivo(master=ventana)
app.mainloop()

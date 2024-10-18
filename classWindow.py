
import tkinter as tk

class Window:
    __ancho = 500
    __alto = 500
    __titulo = "Test"
    __resize = False

    def set_dimensions(self, width, height):
        self.__ancho = width
        self.__alto = height

    def get_dimensions(self):
        return [self.__ancho, self.__alto]

    def set_resize(self, resize):
        self.__resize = resize

    def get_resize(self):
        return self.__resize

    def set_title(self, titulo):
        self.__titulo = titulo

    def get_title(self):
        return self.__titulo

    def crear_ventana(self):
        # Crear la ventana principal
        ventana = tk.Tk()

        ventana.title(self.__titulo)

        # Establecer el tamaño de la ventana (n x m píxeles)
        ventana.geometry(f"{self.__ancho}x{self.__alto}")

        # Evitar que la ventana sea redimensionable
        ventana.resizable(self.__resize, self.__resize)

        # Iniciar el bucle principal de la ventana
        ventana.mainloop()



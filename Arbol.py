import graphviz

# get current time
import time


class Arbol:
    def __init__(self):        
        self.dot = graphviz.Digraph(comment=f"Bruce Castillo 202203069")
        self.dot.attr('node', style='filled', fillcolor='lightblue', fontcolor='black', shape='ellipse')
        self.counter = 0
        self.nodos={}

    def agregarConfiguracion(self, confg):
        self.dot.attr(
            "node",
            style="filled",
            fillcolor=confg["fondo"],
            fontcolor=confg["fuente"],
            shape=confg["forma"],
        )

    def agregarNodo(self, valor):
        nombre = f"nodo{self.counter}"
        self.dot.node(nombre, valor)
        self.counter += 1
        return nombre

    def eliminarNodo(self):
        nombre = f"nodo{self.counter}"
        if nombre in self.nodos:
            del self.nodos[nombre]  # Eliminar el nodo del diccionario
            self.dot.node(nombre, None)  # Eliminar el nodo en la representación gráfica
        self.counter -= 1

    def agregarArista(self, nodo1: str, nodo2: str):
        self.dot.edge(nodo1, nodo2)

    def generarGrafica(self):
        self.dot.render("Reporte", view=True)
        self.dot.save("Reporte.dot")

    def obtenerUltimoNodo(self):
        return f"nodo{self.counter - 1}"


arbol = Arbol()

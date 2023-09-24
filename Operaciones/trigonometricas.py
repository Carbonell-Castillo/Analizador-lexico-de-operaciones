from Operaciones.expresion import *
import math
from Arbol import *


class ExpresionTrigonometrica(Expresion):
    def __init__(self, tipo, valor, linea, columna):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
        self.columna = columna

    def interpretar(self):
        valor = self.valor

        # nombre de las etiquetas
        nodo = None

        # validar si es un numero o una Expresion
        if isinstance(self.valor, Expresion):
            valor = self.valor.interpretar()
            nodo = arbol.obtenerUltimoNodo()
        else:
            valor = self.valor
            if isinstance(valor, (int, float)):
                nodo = arbol.agregarNodo(str(valor))
        
        if isinstance(valor, (int, float)):
            print("-" * 20)
            print("tipo: ", self.tipo)
            print("valor: ", valor)
            resultado = None
            if self.tipo == "seno":
                resultado = round(math.sin(valor),2)
            elif self.tipo == "coseno":
                resultado = round(math.cos(valor),2)
            elif self.tipo == "tangente":
                if abs(valor % (2 * 3.141592653589793)) == (3.141592653589793 / 2):
                    raise ValueError("Tangente indefinida para múltiplos de pi/2.")
                resultado = round(math.tan(valor),2)
            elif self.tipo == "inverso":
                if valor == 0:
                    raise ZeroDivisionError("No se puede calcular el inverso de cero.")
                resultado= round(1/valor, 2)
            
        if resultado is not None:            
            print("El resultado es: ", resultado)
            print("-" * 20)
            # GRAFICAR
            raiz = arbol.agregarNodo(f"{self.tipo}\\n{str(round(resultado,2))}")
            arbol.agregarArista(raiz, nodo)

            return round(resultado, 2)

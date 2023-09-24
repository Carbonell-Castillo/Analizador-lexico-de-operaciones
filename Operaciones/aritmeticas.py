from Operaciones.expresion import *
from Arbol import *
from utilidades import generar_error
import math


class ExpresionAritmetica(Expresion):
    def __init__(self, tipo, valor1, valor2, linea, columna):
        self.tipo = tipo
        self.valor1 = valor1
        self.valor2 = valor2
        self.linea = linea
        self.columna = columna
    contador=1
    def interpretar(self):
        global arbol, contador
        valor1 = self.valor1
        valor2 = self.valor2

        # nombre de las etiquetas
        nodo1 = None
        nodo2 = None

        # validar si es un numero o una Expresion
        if isinstance(self.valor1, Expresion):
            valor1 = self.valor1.interpretar()
            nodo1 = arbol.obtenerUltimoNodo()
        else:
            valor1 = self.valor1
            if self.contador<=1:
                if isinstance(valor1, (int, float)):
                    nodo1 = arbol.agregarNodo(str(valor1))
                    self.contador+=1
            else:
                if isinstance(valor2, (int, float)) and isinstance(valor1, (int, float)):
                    nodo1 = arbol.agregarNodo(str(valor1))
                    self.contador+=1
                else:
                    self.contador-=1
                    arbol.eliminarNodo()

            

        if isinstance(self.valor2, Expresion):
            valor2 = self.valor2.interpretar()
            nodo2 = arbol.obtenerUltimoNodo()
            
        else:
            valor2 = self.valor2
            if isinstance(valor2, (int, float)) and isinstance(valor1, (int, float)):
                nodo2 = arbol.agregarNodo(str(valor2))
            else:
                arbol.eliminarNodo()

        
        if isinstance(valor1, (int, float)) and isinstance(valor2, (int, float)):
            print("-" * 20)
            print("tipo: ", self.tipo)
            print("valor1: ", valor1)
            print("valor2: ", valor2)

            resultado = None
            
            if self.tipo.lower() == "suma":
                resultado = valor1 + valor2
            elif self.tipo.lower() == "resta":
                resultado = valor1 - valor2
            elif self.tipo.lower() == "multiplicacion":
                resultado = valor1 * valor2
            elif self.tipo.lower() == "division":
                if valor2 == 0:
                    generar_error("División por cero no permitida", self.linea, self.columna)
                resultado = valor1 / valor2
            elif self.tipo.lower() == "potencia":
                resultado = round(math.pow(valor1, valor2))
            elif self.tipo.lower() == "raiz":
                if valor2 <= 0:
                    generar_error("Raíz cuadrada de un número negativo no permitida", self.linea, self.columna)
                resultado = round(math.pow(valor1, 1 / valor2))
            elif self.tipo.lower() == "modulo":
                resultado = round((valor1 % valor2), 2)
            else:
                generar_error(self.tipo, self.linea, self.columna)



            if resultado is not None:
                print("El resultado es: ", resultado)
                print("-" * 20)
                # GRAFICAR
                if arbol == None:
                    print("arbol es None")

                raiz = arbol.agregarNodo(f"{self.tipo}\\n{str(resultado)}")
                arbol.agregarArista(raiz, nodo1)
                if self.valor2 != None:
                    arbol.agregarArista(raiz, nodo2)

                return round(resultado,2)

    def __str__(self) -> str:
        return (
            super().__str__()
            + " tipo: "
            + self.tipo
            + " valor1: "
            + str(self.valor1)
            + " valor2: "
            + str(self.valor2)
        )

from abc import ABC,abstractmethod

class Abstract_num(ABC):

    def __init__(self,fila,columna):
        self.fila = fila
        self.columna = columna

    @abstractmethod
    def operacion(self, arbol):
        pass


    @abstractmethod
    def obtener_fila(self):
        return self.fila

    @abstractmethod
    def obtener_columna(self):
        return self.columna

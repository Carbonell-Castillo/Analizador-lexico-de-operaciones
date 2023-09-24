import json
from Lexemas import *
lista_errores = []
contadorErrores=1

def generar_error(char, line, col):
    global contadorErrores
    lista_errores.append(Lexema_errores(contadorErrores,"Error lexico:",char,line,col))
    contadorErrores += 1
    print(
        "Error: caracter desconocido:",
        char,
        "en linea:",
        line + 1,
        "columna:",
        col + 1,
        )
    
def limpiarErrores():
    global contadorErrores, lista_errores
    contadorErrores=1
    lista_errores = []

def archivo_salida():
    global lista_errores
    lista_temporal = {}
    lista_temporal["Errores"] = []

    for lista_error in lista_errores:
        lista_temporal["Errores"].append({
            'No.' : lista_error.num,
            'descripcion' : {
                'lexema' : lista_error.lexema,
                'tipo' : lista_error.tipo,
                'columna': lista_error.columna,
                'fila' : lista_error.fila
            }
        })
        
    with open('Errores', 'w') as file:
        json.dump(lista_temporal,file, indent=4)



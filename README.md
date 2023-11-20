# Analizador lexico de operaciones

## Descripción del Proyecto

Este proyecto consiste en un analizador de lenguaje JSON con funcionalidades de análisis léxico, interpretación de expresiones aritméticas y trigonométricas, generación de árboles de análisis, y manejo de errores. La interfaz de usuario proporciona la capacidad de cargar archivos JSON, realizar análisis y visualizar resultados de manera intuitiva.

## Estructura de Archivos

La organización del proyecto es la siguiente:

```
proyecto/
    ├── App.py
    ├── utilidades.py
    ├── Lexemas.py
    ├── Arbol.py
    ├── abstract_num.py
    ├── Operaciones/
    │   ├── aritmeticas.py
    │   ├── expresion.py
    │   └── trigonometricas.py
```

## Funcionalidades Clave

### `App.py`

- Interfaz de usuario que permite cargar, analizar y visualizar archivos JSON.
- Operaciones de apertura y guardado de archivos.
- Análisis de expresiones aritméticas y trigonométricas.
- Visualización gráfica de árboles de análisis.

### `analizador.py`

- Tokenización de cadenas y números.
- Manejo de errores y generación de archivo de errores.
- Obtención de instrucciones a partir de tokens.

### `Lexemas.py`

- Clases `Lexema` y `Lexema_errores` para representar lexemas y errores.

### `Arbol.py`

- Clase `Arbol` para la creación y representación gráfica de árboles de análisis.

### `abstract_num.py`

- Clase abstracta `Abstract_num` base para las clases en `Lexemas.py`.

### `Operaciones/aritmeticas.py`, `Operaciones/expresion.py`, `Operaciones/trigonometricas.py`

- Clases para expresiones aritméticas y trigonométricas.
- Interpretación de expresiones y generación de árboles de análisis.

## Uso

1. Ejecutar `App.py` para abrir la interfaz de usuario.
2. Cargar un archivo JSON mediante las opciones de archivo.
3. Realizar análisis de expresiones y visualizar resultados.
4. Guardar resultados y árboles generados según sea necesario.

## Conclusiones

Este proyecto ofrece una solución completa para el análisis de lenguaje JSON, proporcionando una interfaz amigable y funcionalidades robustas. Facilita la carga y análisis de archivos JSON, brindando una representación gráfica clara de la estructura de las expresiones y la generación de árboles de análisis.


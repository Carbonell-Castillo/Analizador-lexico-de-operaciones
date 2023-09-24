# Manual Técnico

## Introducción

Este manual técnico proporciona una descripción detallada de la estructura y funcionamiento del proyecto de análisis de lenguaje JSON. El proyecto se divide en varios archivos y módulos que realizan diversas tareas, incluido el análisis léxico, la interpretación de expresiones aritméticas y trigonométricas, la generación de árboles de análisis y la gestión de errores.

## Estructura de Archivos

El proyecto se divide en varios archivos y carpetas organizados de la siguiente manera:

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

A continuación, se explicará cada uno de los archivos y módulos importantes en detalle.

## `App.py`

Este archivo es la interfaz de usuario de la aplicación y maneja la interacción del usuario con el analizador JSON.

```python
# ... Código anterior ...

class MainWindow:
    def __init__(self, root):
        # Inicializa la ventana principal de la aplicación.
        self.root = root
        self.root.title("Analizador")
        self.path = None
        self.conteo_linea = 1

        # Crea los widgets de la GUI.
        self.create_widgets()
        self.create_menu()

    # ... Código anterior ...
```

Este fragmento de código define la clase `MainWindow`, que representa la ventana principal de la aplicación. En su constructor, se inicializa la ventana y se crean los widgets de la interfaz de usuario, como la caja de texto, los menús y el número de línea.
### Clase `MainWindow`

La clase `MainWindow` representa la ventana principal de la aplicación.

#### Constructor `__init__`

- Inicializa la ventana principal y define su título.
- Crea widgets y menús.
- Llama a los métodos `create_widgets()` y `create_menu()` para crear la interfaz de usuario y los menús.

#### Método `create_widgets`

- Crea una ventana con un área de texto y un número de línea.
- Configura el enlace de eventos para actualizar el número de línea cuando el usuario escribe o usa la rueda del mouse.

#### Método `create_menu`

- Crea un menú en la parte superior de la ventana con opciones de "Archivo" y "Acciones".
- Proporciona opciones como abrir, guardar, analizar y mostrar errores.

```python
# ... Código anterior ...

    def actualizar_linea_num(self, event=None):
        conteo = self.widget.get('1.0', tk.END).count('\n')
        if conteo != self.conteo_linea:
            self.linea_numero.config(state=tk.NORMAL)
            self.linea_numero.delete(1.0, tk.END)
            for line in range(1, conteo + 1):
                self.linea_numero.insert(tk.END, f"{line}\n")
            self.linea_numero.config(state=tk.DISABLED)
            self.conteo_linea = conteo
    

    def open_file(self):
        path = filedialog.askopenfilename(filetypes=[("Archivos json", "*.json")])
        if path:
            self.path = path
            with open(path, 'r') as file:
                content_json = file.read()
                self.widget.delete(1.0, tk.END)
                self.widget.insert(tk.END, content_json)
            self.actualizar_linea_num()

    def save_file(self):
        if self.path:
            content_json = self.widget.get(1.0, tk.END)
            with open(self.path, 'w') as file:
                file.write(content_json)
            messagebox.showinfo("Guardado", "Archivo guardado de manera correcta.")

    def save_file_as(self):
        path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos", "*.json")])
        if path:
            self.path = path
            content_json = self.widget.get(1.0, tk.END)
            with open(path, 'w+') as file:
                file.write(content_json)
            messagebox.showinfo("Guardado", "Archivo guardado correctamente")


    # ... Código anterior ...
```
#### Método `actualizar_linea_num`

- Actualiza el número de línea en función del contenido del área de texto.

#### Métodos `open_file`, `save_file` y `save_file_as`

- Permiten al usuario abrir y guardar archivos JSON.
- Actualizan el contenido del área de texto y manejan las operaciones de archivo.

```python
# ... Código anterior ...

    def analyze(self):
        global arbol
        print("Analizando...")
        content_json = self.widget.get(1.0, tk.END).lower()
        limpiarTodo()
        limpiarErrores()
        arbol = analizar(content_json)
        
    def show_errors(self):
        try:
            messagebox.showinfo("Generado","Se generó correctamente el archivo json")
            archivo_salida()
        except:
            messagebox.showinfo("Error","no se ha ingresado ningún archivo")

    def report(self):
        try:
            messagebox.showinfo("Generado", "Se generó correctamente el archivo json")
            content_json = self.widget.get(1.0, tk.END)
            arbol= generarArbol(content_json)
            arbol.generarGrafica()
        except:
            messagebox.showinfo("Error", "No se ha ingresado ningún archivo")
    # ... Código anterior ...
```

#### Método `analyze`

- Realiza el análisis del contenido JSON ingresado en el área de texto.
- Llama a la función `analizar` de `analizado.py`.
- Limpia los errores y el árbol anterior si los hubiera.

#### Método `show_errors`

- Muestra información sobre la generación del archivo JSON y maneja errores.
- Llama a la función `archivo_salida` de `utilidades.py` para generar el archivo JSON.

#### Método `report`

- Muestra información sobre la generación del archivo JSON y maneja errores.
- Llama a la función `generarArbol` de `analizado.py` para crear el árbol y generar la representación gráfica.

### Función Principal `main`

- Inicializa la aplicación y entra en el bucle principal de la interfaz gráfica.

## `analizador.py`

Este archivo contiene la lógica para analizar el lenguaje JSON y generar un árbol de análisis.

### Función `tokenize_string`:

```python
# formar un string
def tokenize_string(input_str, i):
    token = ""
    for char in input_str:
        if char == '"':
            return [token, i]
        token += char
        i += 1
    print("Error: string no cerrado")
```

Esta función se encarga de tokenizar una cadena entre comillas dobles y devuelve el token y la posición del cierre de comillas. Si la cadena no se cierra correctamente, imprime un mensaje de error.

### Función `tokenize_number`:

```python
# formar un numero
def tokenize_number(input_str, i):
    token = ""
    isDecimal = False
    for char in input_str:
        if char.isdigit():
            token += char
            i += 1
        elif char == "." and not isDecimal:
            token += char
            i += 1
            isDecimal = True
        else:
            break
    if isDecimal:
        return [float(token), i]
    return [int(token), i]
```

Esta función se encarga de tokenizar un número, ya sea entero o decimal. Detecta los dígitos y el punto decimal y construye el número correspondiente.

### Función `tokenize_input`:

```python
# formar los tokens
def tokenize_input(input_str):
    # referenciar las variables globales
    global line, col, tokens, contador
    # iterar sobre cada caracter del input
    i = 0
    # mientras no se llegue al final del input
    while i < len(input_str):
        # obtener el caracter actual
        char = input_str[i]
        if char.isspace():
            # si es un salto de linea
            if char == "\n":
                line += 1
                col = 1
            # si es un tabulador
            elif char == "\t":
                col += 4
            # si es un espacio
            else:
                col += 1
            # incrementar el indice
            i += 1
        # si es un string formar el token
        elif char == '"':
            string, pos = tokenize_string(input_str[i + 1 :], i)
            col += len(string) + 1
            i = pos + 2
            token = Token(string, line, col)
            tokens.append(token)
        # ... (otros casos)
        else:
            print("Err: ", line, "ss ", col)
            generar_error(char,line,col)
            i += 1
            col += 1
```

Esta función tokeniza la entrada JSON. Itera a través de los caracteres y llama a las funciones `tokenize_string` y `tokenize_number` cuando se encuentran comillas dobles o números, respectivamente. También maneja espacios, tabuladores y otros caracteres.

### Función `get_instruccion`:

```python
def get_instruccion():
    global tokens, line, col
    operacion = None
    value1 = None
    value2 = None
    while tokens:
        token = tokens.pop(0)
        if token.value == "operacion":
            # eliminar el :
            tokens.pop(0)
            operacion = tokens.pop(0).value
        elif token.value == "valor1":
            # eliminar el :
            tokens.pop(0)
            value1 = tokens.pop(0).value
            if value1 == "[":
                value1 = get_instruccion()
        elif token.value == "valor2":
            tokens.pop(0)
            value2 = tokens.pop(0).value
            if value2 == "[":
                value2 = get_instruccion()
        elif token.value in ["texto", "fondo", "fuente", "forma"]:
            tokens.pop(0)
            configuracion[token.value] = tokens.pop(0).value
        if operacion and value1 and value2:
            return ExpresionAritmetica(operacion, value1, value2, line, col)
        if operacion and operacion in ["seno", "coseno", "tangente", "inverso"] and value1:
            return ExpresionTrigonometrica(operacion, value1, line, col)
    return None
```

Esta función se utiliza para obtener instrucciones a partir de los tokens. Itera a través de los tokens y crea instancias de las clases `ExpresionAritmetica` o `ExpresionTrigonometrica` según la operación y los valores proporcionados.


### Función `generar_error`

- Recibe un carácter `char`, así como la línea y columna donde ocurrió el error.
- Agrega un objeto `Lexema_errores` a la lista `lista_errores` para registrar el error.
- Incrementa el contador de errores `contadorErrores`.
- Imprime un mensaje de error en la consola.

### Función `limpiarErrores`

- Reinicia el contador de errores `contadorErrores` y vacía la lista `lista_errores`.

### Función `archivo_salida`

- Genera un archivo JSON llamado "Errores" que contiene información sobre los errores detectados durante el análisis.
- Convierte los objetos `Lexema_errores` en un formato JSON y los guarda en el archivo.

## `Lexemas.py`

Este archivo define dos clases `Lexema` y `Lexema_errores` utilizadas para representar lexemas y errores respectivamente.

### Clase `Lexema`

- Representa un lexema válido en el lenguaje JSON.
- Almacena el lexema, fila y columna donde se encuentra en el archivo.
- Define un método `operacion` que simplemente devuelve el lexema.
- Proporciona métodos para obtener la fila y columna.

### Clase `Lexema_errores`

- Representa un error léxico detectado durante el análisis.
- Almacena el número de error, tipo de error, lexema erróneo, fila y columna donde ocurrió.
- Define un método `operacion` que devuelve el lexema erróneo.
- Proporciona métodos para obtener la fila y columna.

## `Arbol.py`

Este archivo contiene la clase `Arbol`, que se utiliza para crear y representar gráficamente un árbol de análisis.

### Clase `Arbol`

- Inicializa un objeto `Dot` de Graphviz para generar la representación gráfica del árbol.
- Configura un estilo predeterminado para los nodos del árbol.
- Lleva un contador para asignar nombres únicos a los nodos.
- Proporciona métodos para agregar configuraciones, nodos, aristas y generar la gráfica.
- Guarda el árbol en archivos con extensión `.dot` y visualiza la representación gráfica.

## `abstract_num.py`

Este archivo define una clase abstracta `Abstract_num` que sirve como base para las clases `Lexema` y `Lexema_errores` en `Lexemas.py`.

### Clase Abstracta `Abstract_num`

- Define una clase abstracta con métodos abstractos `operacion`, `obtener_fila`, y `obtener_columna`.
- Tiene un constructor que almacena la fila y columna donde se encuentra el objeto en el archivo.
- `operacion` es un método abstracto que debe ser implementado en las clases derivadas.
- `obtener_fila` y `obtener_columna` son métodos abstractos para obtener la fila y columna.

Aquí están las adiciones al manual técnico para los archivos `Operaciones/aritmeticas.py`, `Operaciones/expresion.py`, y `Operaciones/trigonometricas.py`:

## `Operaciones/aritmeticas.py`

Este archivo define la clase `ExpresionAritmetica`, que representa expresiones aritméticas como suma, resta, multiplicación, división, potencia, raíz y módulo.

### Fragmento de código de `Operaciones/aritmeticas.py`:

```python
class ExpresionAritmetica(Expresion):
    def __init__(self, tipo, valor1, valor2, linea, columna):
        # Constructor de la clase ExpresionAritmetica.
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

        # ... Código para la interpretación de expresiones aritméticas ...

        if isinstance(valor1, (int, float)) and isinstance(valor2, (int, float)):
            # Realiza la operación aritmética según el tipo especificado.
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
            # ... Más operaciones aritméticas ...

            if resultado is not None:
                # Registra el resultado y lo agrega al árbol de análisis.
                print("El resultado es: ", resultado)
                # GRAFICAR - Agrega el resultado al árbol de análisis.
                if arbol == None:
                    print("arbol es None")

                raiz = arbol.agregarNodo(f"{self.tipo}\\n{str(resultado)}")
                arbol.agregarArista(raiz, nodo1)
                if self.valor2 != None:
                    arbol.agregarArista(raiz, nodo2)

                return round(resultado,2)
```


### Clase `ExpresionAritmetica`

- `__init__(self, tipo, valor1, valor2, linea, columna)`: Constructor de la clase que recibe el tipo de operación, los valores de operandos, y la línea y columna donde se encuentra la expresión en el archivo.
- `interpretar(self)`: Método que interpreta la expresión aritmética y devuelve el resultado de la operación.
  - Valida si los valores son números válidos y si la operación es válida (por ejemplo, división por cero o raíz cuadrada de un número negativo).
  - Realiza la operación y devuelve el resultado.
  - Gráfica la expresión en el árbol.
- `__str__(self)`: Método que devuelve una representación de cadena de la expresión aritmética.

## `Operaciones/expresion.py`

Este archivo define la clase abstracta `Expresion` que sirve como base para las clases de expresiones aritméticas y trigonométricas.

### Clase abstracta `Expresion`

- `interpretar(self, contexto)`: Método abstracto que debe ser implementado en las clases derivadas para interpretar la expresión.

## `Operaciones/trigonometricas.py`

Este archivo define la clase `ExpresionTrigonometrica`, que representa expresiones trigonométricas como seno, coseno, tangente e inverso.

```python
class ExpresionTrigonometrica(Expresion):
    def __init__(self, tipo, valor, linea, columna):
        # Constructor de la clase ExpresionTrigonometrica.
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
        self.columna = columna

    def interpretar(self):
        valor = self.valor

        # ... Código para la interpretación de expresiones trigonométricas ...

        if resultado is not None:
            # Registra el resultado y lo agrega al árbol de análisis.
            print("El resultado es: ", resultado)
            # GRAFICAR - Agrega el resultado al árbol de análisis.
            raiz = arbol.agregarNodo(f"{self.tipo}\\n{str(round(resultado,2))}")
            arbol.agregarArista(raiz, nodo)

            return round(resultado, 2)
```


### Clase `ExpresionTrigonometrica`

- `__init__(self, tipo, valor, linea, columna)`: Constructor de la clase que recibe el tipo de operación trigonométrica, el valor del ángulo, y la línea y columna donde se encuentra la expresión en el archivo.
- `interpretar(self)`: Método que interpreta la expresión trigonométrica y devuelve el resultado de la operación.
  - Valida si el valor es un número válido.
  - Realiza la operación trigonométrica correspondiente y devuelve el resultado.
  - Gráfica la expresión en el árbol.

Estas clases y métodos permiten interpretar y calcular expresiones aritméticas y trigonométricas, gestionando errores y registrando la estructura del árbol de análisis de manera adecuada.

## Conclusiones

Este proyecto de análisis de lenguaje JSON demuestra la implementación de un analizador léxico y un generador de árboles de análisis. Además, permite a los usuarios interactuar con una GUI para cargar archivos JSON, analizarlos y visualizar informes gráficos.

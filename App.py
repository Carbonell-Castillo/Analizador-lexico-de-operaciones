import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename
from analizador import analizar, generarArbol, limpiarTodo
from utilidades import archivo_salida, limpiarErrores

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador")
        self.path = None
        self.conteo_linea = 1

        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        self.linea_numero = tk.Text(self.root, width=2, padx=2, takefocus=0, border=0, background='black', state='disabled')
        self.linea_numero.pack(side=tk.LEFT, fill=tk.Y)
        self.linea_numero.config(fg='white')
        self.widget = ScrolledText(self.root, wrap=tk.WORD, width=100, height=20)
        self.widget.pack(expand=True, fill='both')

        self.widget.bind('<Key>', self.actualizar_linea_num)
        self.widget.bind('<MouseWheel>', self.actualizar_linea_num)
    
    def create_menu(self):
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Guardar", command=self.save_file)
        file_menu.add_command(label="Guardar Como", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.quit)

        action_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Acciones", menu=action_menu)
        action_menu.add_command(label="Analizar", command=self.analyze)
        action_menu.add_command(label="Errores", command=self.show_errors)
        action_menu.add_command(label="Reporte", command=self.report)

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

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

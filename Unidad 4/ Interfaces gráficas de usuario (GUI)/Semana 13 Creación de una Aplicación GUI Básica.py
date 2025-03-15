import tkinter as tk
from tkinter import ttk


class DataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Datos")
        self.root.geometry("400x400")

        # Etiqueta y campo de entrada
        self.label = tk.Label(root, text="Ingrese un dato:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        # Botón para agregar datos
        self.add_button = tk.Button(root, text="Agregar", command=self.add_data)
        self.add_button.pack(pady=5)

        # Tabla para mostrar los datos
        self.tree = ttk.Treeview(root, columns=("Dato"), show="headings")
        self.tree.heading("Dato", text="Datos ingresados")
        self.tree.pack(pady=5, fill=tk.BOTH, expand=True)

        # Botón para limpiar la tabla
        self.clear_button = tk.Button(root, text="Limpiar", command=self.clear_data)
        self.clear_button.pack(pady=5)

    def add_data(self):
        """ Agrega el dato ingresado a la tabla. """
        data = self.entry.get()
        if data:
            self.tree.insert("", "end", values=(data,))
            self.entry.delete(0, tk.END)

    def clear_data(self):
        """ Elimina todos los datos de la tabla. """
        for item in self.tree.get_children():
            self.tree.delete(item)


# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = DataApp(root)
    root.mainloop()

#Aplicación GUI simple para gestionar una lista de tareas

import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("500x400")

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", lambda event: self.add_task())  # Agregar con Enter

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.add_button = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(btn_frame, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

    def add_task(self):
        """Añade una nueva tarea a la lista."""
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingrese una tarea.")

    def complete_task(self):
        """Marca la tarea seleccionada como completada (poniendo un visto)."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            task_text = self.task_listbox.get(selected_index)
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(selected_index, f"✔ {task_text}")
        except IndexError:
            messagebox.showwarning("Selección Vacía", "Seleccione una tarea para marcarla como completada.")

    def delete_task(self):
        """Elimina la tarea seleccionada."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Selección Vacía", "Seleccione una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

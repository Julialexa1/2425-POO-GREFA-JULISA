#Aplicación GUI para Gestión de Tareas con Atajos de Teclado

import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Vacía", "Por favor, ingrese una tarea.")

def mark_completed(event=None):
    try:
        selected_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_index)
        if not task.startswith("✔ "):
            task_listbox.delete(selected_index)
            task_listbox.insert(selected_index, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Selección Inválida", "Seleccione una tarea para marcar como completada.")

def delete_task(event=None):
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Selección Inválida", "Seleccione una tarea para eliminar.")

def close_app(event=None):
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x400")

# Campo de entrada de tareas
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)
task_entry.bind("<Return>", add_task)

# Botones de acción
btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Añadir Tarea", command=add_task).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Marcar Completada", command=mark_completed).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Eliminar Tarea", command=delete_task).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Salir", command=close_app).grid(row=0, column=3, padx=5)

# Lista de tareas
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Atajos de teclado
root.bind("<s>", mark_completed)
root.bind("<d>", delete_task)
root.bind("<Delete>", delete_task)
root.bind("<Escape>", close_app)

# Iniciar la aplicación
root.mainloop()

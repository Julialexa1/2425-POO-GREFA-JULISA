#Creación de una agenda personal

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi Agenda Personal")
        self.root.geometry("600x500")

        # Frame para ingresar datos
        frame_input = ttk.Frame(root)
        frame_input.pack(pady=10)

        ttk.Label(frame_input, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(frame_input, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_input, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = ttk.Entry(frame_input, width=15)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_input, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = ttk.Entry(frame_input, width=30)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botones
        btn_frame = ttk.Frame(root)
        btn_frame.pack(pady=10)

        self.add_button = ttk.Button(btn_frame, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(row=0, column=0, padx=5)

        self.delete_button = ttk.Button(btn_frame, text="Eliminar Evento", command=self.delete_event)
        self.delete_button.grid(row=0, column=1, padx=5)

        self.exit_button = ttk.Button(btn_frame, text="Salir", command=root.quit)
        self.exit_button.grid(row=0, column=2, padx=5)

        # Tabla de eventos
        self.tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

    def add_event(self):
        date = self.date_entry.get()
        time = self.time_entry.get().strip()
        desc = self.desc_entry.get().strip()

        if not time or not desc:
            messagebox.showwarning("Entrada Inválida", "Por favor, complete todos los campos.")
            return

        self.tree.insert("", "end", values=(date, time, desc))
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def delete_event(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Eliminar Evento", "Seleccione un evento para eliminar.")
            return

        confirm = messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de eliminar este evento?")
        if confirm:
            self.tree.delete(selected_item)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

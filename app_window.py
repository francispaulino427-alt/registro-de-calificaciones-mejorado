import tkinter as tk
from tkinter import ttk, messagebox
from services.student_service import StudentService


class AppWindow(tk.Tk):
    def __init__(self, service: StudentService):
        super().__init__()

        self.service = service

        self.title("Registro de Calificaciones")
        self.geometry("700x550")

        self.create_widgets()

    def create_widgets(self):

        frame = tk.Frame(self)
        frame.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(frame, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_id = tk.Entry(frame)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Nombre:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(frame)
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Asignatura:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_asignatura = tk.Entry(frame)
        self.entry_asignatura.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Calificación:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_calificacion = tk.Entry(frame)
        self.entry_calificacion.grid(row=3, column=1, padx=5, pady=5)

        btn = tk.Button(
            self,
            text="Registrar Estudiante",
            command=self.create_student,
            bg="#4CAF50",
            fg="white"
        )
        btn.grid(row=1, column=0, pady=10)

        self.tree = ttk.Treeview(
            self,
            columns=("id", "nombre", "asignatura", "calificacion", "estado"),
            show="headings"
        )

        columnas = [
            ("id", "ID"),
            ("nombre", "Nombre"),
            ("asignatura", "Asignatura"),
            ("calificacion", "Calificación"),
            ("estado", "Estado"),
        ]

        for col, texto in columnas:
            self.tree.heading(col, text=texto)
            self.tree.column(col, anchor="center", width=120)

        self.tree.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.render_table()

    def create_student(self):
        try:
            self.service.create_one(
                self.entry_id.get(),
                self.entry_nombre.get(),
                self.entry_asignatura.get(),
                self.entry_calificacion.get()
            )

            self.render_table()

            self.entry_id.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)
            self.entry_asignatura.delete(0, tk.END)
            self.entry_calificacion.delete(0, tk.END)

            self.entry_id.focus()

        except Exception as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def render_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for s in self.service.find_all():
            self.tree.insert(
                "",
                "end",
                values=(
                    s.id,
                    s.nombre,
                    s.asignatura,
                    s.calificacion,
                    s.estado
                )
            )

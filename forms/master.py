import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import re

class App:

    def cerrar_sesion(self):
        self.ventana.destroy()
        from forms.login import Login_Form
        Login_Form()

    def exitFullScreen(self, event):
        self.ventana.attributes("-fullscreen", False)

    def guardar_paciente(self):
        numero_sc = self.nss.get()
        nombre = self.nombre.get()
        genero = self.genero.get()
        fecha_nacimiento = self.fecha_nacimiento.get()
        correo_electronico = self.correo_electronico.get()
        telefono = self.telefono.get()

        if numero_sc == "" or nombre == "" or genero == "" or fecha_nacimiento == "" or telefono == "":
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        try:
            conn = sqlite3.connect('./db/medvault.db')
            cursor = conn.cursor()

            # Verificar si el paciente ya está registrado
            cursor.execute('''SELECT * FROM paciente WHERE numero_sc = ?''', (numero_sc,))
            paciente_existente = cursor.fetchone()

            if paciente_existente:
                messagebox.showwarning("Advertencia", "El paciente ya está registrado.")
                return

            # Insertar nuevo paciente
            cursor.execute('''INSERT INTO paciente (numero_sc, nombre, genero, fecha_nacimiento, correo_electronico, telefono) VALUES (?, ?, ?, ?, ?, ?)''', (numero_sc, nombre, genero, fecha_nacimiento, correo_electronico, telefono))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Paciente registrado exitosamente.")
            self.mostrar_pacientes_guardados()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar el paciente: {e}")

    def mostrar_pacientes_guardados(self):
        self.lista_pacientes.delete(0, tk.END)
        try:
            conn = sqlite3.connect('./db/medvault.db')
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM paciente''')
            pacientes = cursor.fetchall()
            conn.close()

            if pacientes:
                for paciente in pacientes:
                    self.lista_pacientes.insert(tk.END, f"{paciente[1]} - {paciente[0]}")
            else:
                self.lista_pacientes.insert(tk.END, "No hay pacientes registrados.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener la lista de pacientes: {e}")

    def obtener_info_paciente(self):
        numero_sc = self.nss.get()
        if not numero_sc:
            messagebox.showwarning("Advertencia", "Por favor, ingrese el NSS del paciente.")
            return

        try:
            conn = sqlite3.connect('./db/medvault.db')
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM paciente WHERE numero_sc = ?''', (numero_sc,))
            paciente = cursor.fetchone()
            conn.close()

            if paciente:
                self.mostrar_info_paciente(paciente)
            else:
                messagebox.showwarning("Advertencia", "Paciente no encontrado.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener la información del paciente: {e}")

    def mostrar_info_paciente(self, paciente):
        ventana_info_paciente = tk.Toplevel()
        ventana_info_paciente.title("Información del Paciente")
        ventana_info_paciente.geometry("400x300")

        frame_info = tk.Frame(ventana_info_paciente, bd=2, relief=tk.SOLID, bg="#fcfcfc")
        frame_info.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        etiqueta_nombre = tk.Label(frame_info, text="Nombre:", font=("Arial", 12), bg="#fcfcfc")
        etiqueta_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        valor_nombre = tk.Label(frame_info, text=paciente[1], font=("Arial", 12), bg="#fcfcfc")
        valor_nombre.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        etiqueta_genero = tk.Label(frame_info, text="Género:", font=("Arial", 12), bg="#fcfcfc")
        etiqueta_genero.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        valor_genero = tk.Label(frame_info, text=paciente[2], font=("Arial", 12), bg="#fcfcfc")
        valor_genero.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        etiqueta_fecha = tk.Label(frame_info, text="Fecha de Nacimiento:", font=("Arial", 12), bg="#fcfcfc")
        etiqueta_fecha.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        valor_fecha = tk.Label(frame_info, text=paciente[3], font=("Arial", 12), bg="#fcfcfc")
        valor_fecha.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        etiqueta_correo = tk.Label(frame_info, text="Correo Electrónico:", font=("Arial", 12), bg="#fcfcfc")
        etiqueta_correo.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        valor_correo = tk.Label(frame_info, text=paciente[4], font=("Arial", 12), bg="#fcfcfc")
        valor_correo.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        etiqueta_telefono = tk.Label(frame_info, text="Teléfono:", font=("Arial", 12), bg="#fcfcfc")
        etiqueta_telefono.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        valor_telefono = tk.Label(frame_info, text=paciente[5], font=("Arial", 12), bg="#fcfcfc")
        valor_telefono.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.attributes("-fullscreen", True)
        self.ventana.bind("<Escape>", self.exitFullScreen)

        # Carga de la imagen de fondo
        self.background_image = Image.open("./images/logo.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        
        # Creamos un label para la imagen de fondo
        self.background_label = tk.Label(self.ventana, image=self.background_photo, bg="#fcfcfc")
        self.background_label.place(relwidth=1, relheight=1)

        # Creación del frame principal
        frame = tk.Frame(self.ventana, bg="#fcfcfc")
        frame.place(relx=0.5, rely=0.1, anchor="n")

        # Etiqueta y campo de entrada para NSS
        etiqueta_nss = tk.Label(frame, text="NSS", font=("Arial", 14), bg="#fcfcfc", bd=0)
        etiqueta_nss.grid(row=0, column=0, padx=(20, 10), pady=10)
        self.nss = ttk.Entry(frame, font=("Arial", 14), background="#fcfcfc", validate="key")
        self.nss['validatecommand'] = (self.nss.register(self.validate_nss), '%P')
        self.nss.grid(row=0, column=1, padx=(0, 10), pady=10)

        # Botón para buscar paciente por NSS
        buscar = tk.Button(frame, text="Buscar", font=("Arial", 14), bg="#fcfcfc", command=self.obtener_info_paciente, highlightthickness=0)
        buscar.grid(row=0, column=2, padx=10, pady=10)

        # Etiqueta y campo de entrada para Nombre
        etiqueta_nombre = tk.Label(frame, text="Nombre", font=("Arial", 14), bg="#fcfcfc", bd=0)
        etiqueta_nombre.grid(row=1, column=0, padx=(20, 10), pady=10)
        self.nombre = tk.StringVar()
        self.entry_nombre = ttk.Entry(frame, textvariable=self.nombre, font=("Arial", 14), background="#fcfcfc")
        self.entry_nombre.grid(row=1, column=1, padx=(0, 10), pady=10)

        # Etiqueta y campo de entrada para Género
        etiqueta_genero = tk.Label(frame, text="Género", font=("Arial", 14), bg="#fcfcfc", bd=0)
        etiqueta_genero.grid(row=1, column=2, padx=(10, 20), pady=10)
        self.genero = tk.StringVar()
        self.entry_genero = ttk.Combobox(frame, textvariable=self.genero, font=("Arial", 14), state="readonly")
        self.entry_genero["values"] = ("Hombre", "Mujer")
        self.entry_genero.grid(row=1, column=3, padx=(0, 10), pady=10)

        # Etiqueta y campo de entrada para Fecha de Nacimiento
        etiqueta_fecha = tk.Label(frame, text="Fecha de Nacimiento", font=("Arial", 14), bg="#fcfcfc", bd=0)
        etiqueta_fecha.grid(row=2, column=0, padx=(20, 10), pady=10)
        self.fecha_nacimiento = tk.StringVar()
        self.entry_fecha = ttk.Entry(frame, textvariable=self.fecha_nacimiento, font=("Arial", 14), background="#fcfcfc")
        self.entry_fecha.grid(row=2, column=1, padx=(0, 10), pady=10)

        # Etiqueta y campo de entrada para Correo Electrónico
        etiqueta_correo = tk.Label(frame, text="Correo Electrónico", font=("Arial", 14), bg="#fcfcfc", bd=0)
        etiqueta_correo.grid(row=2, column=2, padx=(10, 20), pady=10)
        self.correo_electronico = tk.StringVar()
        self.entry_correo = ttk.Entry(frame, textvariable=self.correo_electronico, font=("Arial", 14), background="#fcfcfc")
        self.entry_correo.grid(row=2, column=3, padx=(0, 10), pady=10)

        # Etiqueta y campo de entrada para Teléfono
        etiqueta_telefono = tk.Label(frame, text="Teléfono", font=("Arial", 14), bg="#fcfcfc", bd=0)
        etiqueta_telefono.grid(row=3, column=0, padx=(20, 10), pady=10)
        self.telefono = tk.StringVar()
        self.entry_telefono = ttk.Entry(frame, textvariable=self.telefono, font=("Arial", 14), background="#fcfcfc")
        self.entry_telefono.grid(row=3, column=1, padx=(0, 10), pady=10)

        # Botón para guardar paciente
        guardar = tk.Button(frame, text="Guardar Paciente", font=("Arial", 14), bg="#fcfcfc", command=self.guardar_paciente, highlightthickness=0)
        guardar.grid(row=4, column=1, padx=10, pady=10)

        # Frame para la lista de pacientes
        frame_pacientes = tk.Frame(self.ventana, bg="#fcfcfc")
        frame_pacientes.place(relx=0.5, rely=0.6, anchor="n", relwidth=0.8, relheight=0.3)

        # Etiqueta para la lista de pacientes
        etiqueta_lista = tk.Label(frame_pacientes, text="Pacientes Guardados", font=("Arial", 14), bg="#fcfcfc", bd=0)
        etiqueta_lista.pack(pady=(10, 5))

        # Lista de pacientes
        self.lista_pacientes = tk.Listbox(frame_pacientes, font=("Arial", 12), width=50, height=5, bg="#fcfcfc", bd=2, relief=tk.SOLID)
        self.lista_pacientes.pack(padx=10, pady=(0, 10))

        # Obtener y mostrar la lista de pacientes al iniciar la aplicación
        self.mostrar_pacientes_guardados()

        # Evento para mostrar la información del paciente al hacer clic en la lista
        self.lista_pacientes.bind("<<ListboxSelect>>", self.obtener_info_paciente)

        # Etiqueta y botón de "cerrar sesión"
        etiqueta_cerrarsesion = tk.Button(self.ventana, text="Cerrar Sesión", font=("Arial", 12), bg="#fcfcfc", bd=0, command=self.cerrar_sesion)
        etiqueta_cerrarsesion.place(relx=1.0, rely=0.0, anchor="ne")

        self.ventana.mainloop()

    def validate_nss(self, new_text):
        return re.match("^[0-9]*$", new_text) is not None


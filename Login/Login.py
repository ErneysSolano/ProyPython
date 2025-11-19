import pyodbc
import bcrypt 
import tkinter as tk 
from tkinter import messagebox

#-----conexion a DB ------------------------------>
def conexDB():
    try:
        conexion = pyodbc.connect(
           'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=(localdb)\\Esolano;'  # o el nombre de tu servidor
            'DATABASE=DBColegio;' 
            'Trusted_Connection=yes;'
        )
        return conexion
    except Exception as e:
        messagebox.showerror("Error de Conexion", f"No se pudo conectar a la base de datos:\n{e}")
        return None
    
#-------------===========================--------------->
def func_logear():
    usuario = inputUsuario.get().strip()
    contrasenna = inputContrasenna.get().strip()
    
    if not usuario or not contrasenna:
        messagebox.showwarning("Campos Vacios","Por favor, Ingresar Usuario y Contraseña")
        return
    
    conexion = conexDB()
    if conexion is None:
        None
     
    try:
        cursor = conexion.cursor()
        
        cursor.execute("select * from Tbl_Usuario where usuario = ? and contrasenna = ?", (usuario, contrasenna))
        fila = cursor.fetchone()
        
        if fila:
            messagebox.showinfo("Login exitoso", f"Bienvenido, {usuario}")
            MenuPrincipal()
        else:
            messagebox.showerror("Error", "Usuario o contraseña Incorrectos")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrio un error:\n{e}")
    finally:
        conexion.close()
        
#----------------------------=============---------- Ventana Menu Principal
        
def MenuPrincipal():
    ventana.withdraw()
    menu = tk.Toplevel()
    menu.title("Menu Prinsipal")
    menu.geometry("300x200")
    menu.config(bg="#f0f4f7")
    
    tk.Label(menu, text="Bienvenido al sistema de logeo",
             bg="#f0f4f7", font=("Segoe UI",11, "bold")).pack(pady=20)
    tk.Button(menu, text="Cerrar Sesion", command=lambda: CerrarSesion(menu),
              bg="#ff4d4d", fg="white", font=("Segoe UI",10,"bold")).pack(pady=20)
    
def CerrarSesion(menu):
    menu.destroy()
    ventana.deiconify()
    

#----------------------------=============---------- Interfaz grafica Login


ventana = tk.Tk()
ventana.title("Sistema de Login")
ventana.geometry("350x230")
ventana.resizable(False, False)
ventana.config(bg="#51d6bc")

# 🔹 Frame principal
frameFormulario = tk.Frame(ventana, bg="#e8eef7", bd=2, relief="solid", padx=10, pady=15)
frameFormulario.pack(pady=25)

#----------------------------------------------
# 🧩 Función para agregar placeholders
def placeholder(entry, texto):
    entry.insert(0, texto)
    entry.config(fg="gray")

    def al_foco(event):
        if entry.get() == texto:
            entry.delete(0, tk.END)
            entry.config(fg="black", show="*" if entry == inputContrasenna else "")

    def fuera_foco(event):
        if entry.get() == "":
            entry.insert(0, texto)
            entry.config(fg="gray", show="")

    entry.bind("<FocusIn>", al_foco)
    entry.bind("<FocusOut>", fuera_foco)

#----------------------------------------------
# Campo Usuario
inputUsuario = tk.Entry(frameFormulario, width=30, font=("Segoe UI", 10))
inputUsuario.pack(pady=8)
placeholder(inputUsuario, "Usuario")

# Campo Contraseña
inputContrasenna = tk.Entry(frameFormulario, width=30, font=("Segoe UI", 10))
inputContrasenna.pack(pady=8)
placeholder(inputContrasenna, "Contraseña")

# Botón
tk.Button(
    ventana,
    text="Iniciar Sesión",
    width=18,
    bg="#1e90ff",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=func_logear
).pack(pady=10)

ventana.mainloop()
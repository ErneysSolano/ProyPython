import tkinter as tk
from tkinter import messagebox

#creo la ventana principal 
ventana = tk.Tk()
ventana.title("VENTANA PRINCIPAL")
ventana.geometry("600x450")#---ancho por alto

listaDatos = []

#-------------------------<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>---------------------------<Diseño Form Princ>-
#Etiquetas---- label---------------------------------------------------------
etiqueta = tk.Label(ventana,text="Nombre")
etiqueta.grid(row=0, column=0, padx=10, pady=10) #--si no coloco esto no aparece el Label

#input--
inputNombre = tk.Entry(ventana)
inputNombre.grid(row=0, column=1, padx=10, pady=10)

etiqueta = tk.Label(ventana,text="Apellido")
etiqueta.grid(row=1, column=0, padx=10, pady=10) #--si no coloco esto no aparece el Label

inputApellido = tk.Entry(ventana)
inputApellido.grid(row=1, column=1, padx=10, pady=10)

etiqueta = tk.Label(ventana,text="Telefono")
etiqueta.grid(row=2, column=0, padx=10, pady=10) #--si no coloco esto no aparece el Labe

inputTelefono = tk.Entry(ventana)
inputTelefono.grid(row=2, column=1, padx=10, pady=10)

#-------------------------<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>---------------------------<Func Guardar>-

def FuncGuardar():
    nombre = inputNombre.get().strip()
    apellido = inputApellido.get().strip()
    telefono = inputTelefono.get().strip()

    if not nombre or not apellido or not apellido:
        messagebox.showerror("Mensaje Error", "Todos los campos son obligatorios")
        return

    listaDatos.append({
        "nombre":nombre,
        "apellido": apellido,
        "Telefono" : telefono
    })

    print("Datos guardados: ", listaDatos)

    messagebox.showinfo("Mensaje Exito", " Registro Exitoso")

    inputNombre.delete(0,tk.END)
    inputApellido.delete(0,tk.END)
    inputTelefono.delete(0, tk.END)

ButtonGuardar = tk.Button(ventana, text="💾 Guardar", command=FuncGuardar)
ButtonGuardar.grid(row=3,column=0,columnspan=5, pady=30)


ventana.mainloop()#---permite que se ejecute la ventana
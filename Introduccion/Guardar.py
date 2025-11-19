class ClsPersona:
    def __init__(self, tipoCC, numeroDoc, nombres, apellidos, edad, correo, sueldo):
        self.tipoCC    = tipoCC
        self.numeroDoc = numeroDoc
        self.nombres   = nombres
        self.apellidos = apellidos
        self.edad      = edad
        self.correo    = correo
        self.sueldo    = sueldo

    def __str__(self):
        return f"Tipo de Documento: {self.tipoCC}, N Documento:{self.numeroDoc}, Nombres: {self.nombres}, Apellidos: {self.apellidos}, Edad: {self.edad}, Correo: {self.correo}, Sueldo: {self.sueldo}"
    
#aqui se declara la lista donde se va alamacenar la informacion
listPersona = []

def AgregarPersona():
    tipoDoc   = input("Ingrese el tipo de Doc: ")
    numeroDoc = input("Ingrese numero de Documento: ")
    nombres   = input("Ingrese los/el nombre: ")
    apellidos =  input("Ingrese el/los  apellido(s): ")
    edad      = input("Ingrese su edad: ")
    correo    = input("Ingrese su correo: ")
    sueldo    = input("Ingrese su sueldo: ") 
    personas  =  ClsPersona(tipoDoc,numeroDoc,nombres,apellidos,edad,correo,sueldo)
    listPersona.append(personas)
    print("Persona agregada correctamente.\n")


def Listarpersonas():
    if not listPersona:
        print("No hay registro.\n")
    else:
        print("\n---REGISTRO DE PERSONAS---")
        for i, persona in enumerate(listPersona, start=1):
            print(f"{i}.{persona}")
        print()

def actualizarPersonas():
    Listarpersonas()
    indice = int(input("Ingrese el numero de la persona a actualizar:  ")) -1
    if 0 <= indice < len(listPersona):
        nombres   = input("Ingrese los/el nuevo nombre: ")
        apellidos =  input("Ingrese el/los nuevo apellido(s): ")
        edad      = input("Ingrese su nueva edad: ")
        correo    = input("Ingrese su nuevo correo: ")
        sueldo    = input("Ingrese su nuevo sueldo: ") 
        listPersona[indice].nombres = nombres
        listPersona[indice].apellidos = apellidos
        listPersona[indice].edad = edad
        listPersona[indice].correo = correo
        listPersona[indice].sueldo = sueldo
        print("Registro actalizado.\n")
    else:
        print("Indice invalido.\n")

def EliminarPersona():
     Listarpersonas()
     indice = int(input("Ingrese el numero de la persona a eliminar:  ")) -1
     if 0 <= indice < len(listPersona):
        listPersona.pop(indice)
        print("Persona Eliminada.\n")
     else:
         print("Indice invalido")

#-------======----Menu Personal --------===-----
while True:
    print("=====MENU======")
    print("1. Agregar Persona")
    print("2. Buscar Persona")
    print("3. Actualizar Persona")
    print("4. Eliminar Persona")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        AgregarPersona()
    elif opcion == "2":
        Listarpersonas()
    elif opcion == "3":
        actualizarPersonas()
    elif opcion == "4":
        EliminarPersona()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion invalida.\n")

 
    
        




"""----------------------------==------------==-----------------------==----------------------------------------------===---------
def ListarRegistro():
    for personas in listPersona:
        print(personas)
#uso de las funciones
AgregarPersona("CC","Erneys David","Solano Cortes", 24, "Daveysolano124@gmail.com", 3250000.0)  
AgregarPersona("CE","Yonaiker David","Alcala Roa", 22, "YoiDavid@gmail.com", 1423500.0)  
ListarRegistro()
"""
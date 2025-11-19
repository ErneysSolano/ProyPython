""" x = "Hello"
y = 15
s = ""

print(bool(x))
print(bool(y))
print(bool(s))

sum1 = 20 + 20
sum2 = sum1 + 30
sum3 = sum2 + 40
#print(  str(sum1) + " | " + str(sum2) + " | " + str(sum3))
print(f"{sum1} | {sum2} | {sum3}")

x = 18
y = 5
sum = x / y
sum2 = x // y
print(f"{sum} | {sum2}")

thislist = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
thislist[1] = "Martes festisvo"
print(thislist)

thislist = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
thislist.append("Sabado")
thislist.insert(0, "Domingo")
#thislist[1:3] = ["Martes Festisvo", "Miercoles Festivo"]
print(thislist)

#--------------------------------------------------lista de bucles----------

listaMes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"] #imprime uno por uno
for x in listaMes:
    print(f"{listaMes.index(x)} | {x}")

listaMes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"] # imprime haciendo referencia al indice
for i in range(len(listaMes)):
    print(listaMes[i])

listaMes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"] 
i = 0
while i <  len(listaMes):
    print(listaMes[i])
    i = i +1
listaMes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"] 
newList = []

for x in listaMes:
    if "o" in x:
        newList.append(x)

print(newList)

lisaAnimal = {"Perro", "Gato", "Caballo", "Cerdo"}
print(lisaAnimal)

thisMoto = {  #---------------------------diccionario
    "Marca" : "XTZ",
    "Modelo" : "2026",
    "Cilindraje" : 250
}

print(thisMoto)

number = -2
if number > 0:
    print("The number is positive")
elif number < 0:
    print("el numero es negativo")


dia = 5  
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4: 
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabados")
    case 7:
        print("Domingo")                        


def saludar():# ---- se declara 
    print("Buenos dias a la funcion")

saludar()    #--- pero se tiene que llamar par que funcione
#---------------------------------------------------------------------->
def nombreCompleto(nombres, apellidos):
    print(f"{nombres}  {apellidos}")

nombreCompleto("Erneys David", "Solano Cortes" )

def pertenece(ubi = "el mundo"):
    print("La persona pertenece a ", ubi)

pertenece("Colombia")
pertenece("Nicaragua")
pertenece()


def Ciudades(*citys): #
    print(f"La ciudad es " + str(citys))

Ciudades("Bogota", "Cali", "Medellin", "Valledupar", "Barranquilla", "Cartagena")


def carro(**mycar): #-----------hace como msi fuera diccionario
    print("Type: ", type(mycar))
    print("Marca ", mycar["marca"])
    print("Modelo", mycar["modelo"])
    print("Anno", mycar["anno"])

carro(marca="Mercedez ben", modelo="mybacht s",anno ="2026")

#-----------------------------------------------------

def changecase(func):
    def wrapper():
        result = func()
        return result.swapcase() #aqui se cambia de miniscula a myuscula y si esta en mayuscula lo cambia miniscula-----------
    return wrapper

@changecase
def fucnt():
    return "Buenas Tardes"
print(fucnt())

#------------------------------------------------------------------>lambda
x = lambda a : a + 23
print(x(5)) # resulytado 28--- esto suma

x = lambda a, b, c : a + b + c
print(x(5, 13, 5)) # resulytado 23--- esto suma multiples valores

def func(n):
    return lambda a : a * n

doublefunc= func(2)

print(doublefunc(11))

"""


#Jueves 11 de Febrero de 2025
#Gomez Trejo Ezequiel

#EJERCICIO COCHE--------------------------------------------------------------------------------------------------------
from clases import Coche

print("\n-----REGISTRO DE MI COCHE-----\n")
id = input("Ingrese el ID del auto: ")
marca = input("Ingrese la marca del auto: ")
modelo = input("Ingrese el modelo del auto: ")
color = input("Ingrese el color del auto: ")

mi_coche = Coche(id, marca, modelo, color)

opcion = None

while opcion != 4:
    print("\nSelecciona una opción\n")
    print("1. Mostrar información de mi coche\n")
    print("2. Aumentar velocidad\n")
    print("3. Disminuir velocidad\n")
    print("4. Salir\n")
    opcion = int(input("\nOpción: "))

    if opcion == 1:
        mi_coche.mostrarInformacion()
    elif opcion == 2:
        mi_coche.aumentarVelocidad()
    elif opcion == 3:
        mi_coche.disminuirVelocidad()
    elif opcion == 4:
        print("\nSaliendo...\n")
    else:
        print("\nOpción no válida\n")

#EJERCICIO CTA BANCARIA------------------------------------------------------------------------------------------------------
from clases import ctaBancaria

print("\n---APERTURA DE CUENTA BANCARIA---\n")
nocta = int(input("Escriba su no. de cliente: "))
titular = input("¿Cuál es su nombre: ")
print("Si desea agregar saldo a su cuenta digite 1")
respuesta = int(input("Respuesta: "))
if respuesta == 1:
    saldo = float(input("Digite la cantidad a ingresar: "))
    print(f"Usted ha ingresado {saldo} pesos")
    mi_cuenta = ctaBancaria(nocta, titular, saldo)
else:
    mi_cuenta = ctaBancaria(nocta, titular, 0)

opcion = None

while opcion != 4:
    print("\nSelecciona una opción\n")
    print("1. Depositar\n")
    print("2. Retirar\n")
    print("3. Consultar Saldo\n")
    print("4. Salir\n")
    opcion = int(input("\nOpción: "))

    if opcion == 1:
        mi_cuenta.depositarDinero()
    elif opcion == 2:
        mi_cuenta.retirarDinero()
    elif opcion == 3:
        mi_cuenta.consultarSaldo()
    elif opcion == 4:
        print("\nSaliendo...\n")
    else:
        print("\nOpción no válida\n")

#EJERCICIO RECTANGULO------------------------------------------------------------------------------------------------------
from clases import Rectangulo

print("\n---ÁREA Y PERÍMETRO DE UN RECTÁNGULO--\n")
ancho = float(input("Digita el ancho del rectángulo: "))
alto = float(input("Digita la altura del rectángulo: "))

rectangulo = Rectangulo(ancho, alto)

opcion = None

while opcion != 4:
    print("\nSelecciona una opción\n")
    print("1. Calcular Área\n")
    print("2. Calcular Perímetro\n")
    print("3. Mostrar Información del Rectángulo\n")
    print("4. Salir\n")
    opcion = int(input("\nOpción: "))

    if opcion == 1:
        rectangulo.calcularArea()
    elif opcion == 2:
        rectangulo.calcularPerimetro()
    elif opcion == 3:
        rectangulo.mostrarInformacion()
    elif opcion == 4:
        print("\nSaliendo...\n")
    else:
        print("\nOpción no válida\n")
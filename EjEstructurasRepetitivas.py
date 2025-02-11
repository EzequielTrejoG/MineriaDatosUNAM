#Martes 11 de Febrero de 2025
#Gomez Trejo Ezequiel   Minería de Datos

#Ejercicio 1: Suma de los primeros N números
print("\n---1. SUMA DE LOS PRIMEROS N NÚMEROS---\n")
try:
    numero = int(input("Escribe un número: "))
    if numero < 0:
        print("\nNo debes ingresar números negativos")
    else:
        suma = 0
        for i in range(1, numero + 1):
            suma += i
        print(f"La suma de los primeros {numero} números naturales es: {suma}")
except:
    print("\nSolo debes ingresar números")

#Ejercicio 2: Factorial de un número
print("\n---2. FACTORIAL DE UN NÚMERO---")
try:
    numero = int(input("Escribe un número entero positivo: "))
    if numero < 0:
        print("\nNo debes ingresar números negativos")
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        print(f"El factorial de {numero} es {factorial}")
except:
    print("\nSolo debes ingresar números")

#Ejercicio 3: Tabla de multiplicar
print("\n---3. TABLAS DE MULTIPLICAR---")
try:
    numero = int(input("Escribe un número para mostrar su tabla de multiplicar: "))
    print(f"\nTABLA DEL {numero}")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
except:
    print("\nSolo debes ingresar números")

#Ejercicio 4: Cálculo de promedio de notas
print("\n---4. PROMEDIO DE NOTAS CON WHILE---")
suma = 0
contador = 0
print("\nDigita tus notas. (Se detiene cuando la nota sea negativa): \n")
try:
    while True:
        nota = float(input("Nota: "))
        if nota < 0:
            break
        else:
            suma += nota
            contador += 1
except:
    print("\nSolo debes ingresar números")

if contador > 0:
    promedio = suma / contador
    print(f"\nEl promedio es de {promedio}")

'''CON CICLO FOR'''
import itertools

print("\n---4. PROMEDIO DE NOTAS CON FOR---")
suma = 0
contador = 0
try:
    print("\nDigita tus notas. (Se detiene cuando la nota sea negativa): \n")
    for i in itertools.count():
        nota = float(input("Nota: "))
        if nota < 0:
            break
        else:
            suma += nota
            contador += 1
    if contador > 0:
        promedio = suma / contador
        print(f"El promedio es de: {promedio}")
except:
    print("\nSolo debes ingresar números")


#Ejercicio 5: Serie de Fibonacci
print("\n---5. SERIE DE FIBONACCI---")
try:
    N = int(input("\nIntroduce el valor de N: "))
    a, b = 0, 1
    print("\nSerie de Fibonacci: \n")
    for i in range(N):
        a, b = b, a + b 
        print(a)
except:
    print("\nSolo debes ingresar números")

#Ejercicio 6: Potencia de un número
print("\n---6. POTENCIA DE UN NÚMERO---")
try:
    base = int(input("\nDigita la base: "))
    exponente = int(input("\nDigita el exponente: "))
    resultado = 1
    for i in range(exponente):
        resultado = resultado * base
    print(f"\nLa potencia de {base} elevado a la {exponente} es {resultado}")
except:
    print("\nSolo debes ingresar números")

#Ejercicio 7: Suma de números pares en un rango
print("\n---7. SUMA DE NÚMEROS PARES EN UN RANGO---")
print("\nIntroduce el valor de A(menor) y B(mayor)")
try:
    a = int(input("\nA: "))
    b = int(input("\nB: "))
    if b < a:
        print("\nEl numero A debe ser menor que el B\n")
    else:
        suma = 0
        for i in range(a, b + 1):
            if i % 2 == 0:
                suma += i
        print(f"\nLos números pares son:")
        for i in range(a, b + 1):
            if i % 2 == 0:
                print(i)
        print(f"La suma de esos números es {suma}\n")
except:
    print("\nSolo debes ingresar números")

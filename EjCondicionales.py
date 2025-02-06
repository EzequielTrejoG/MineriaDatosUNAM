#Jueves 06 de febrero de 2025
#Minería de Datos
#Gomez Trejo Ezequiel   No. Cta = 421003866

# 1.Verificar si un número es par o impar
print("\n---Ej1. PAR O IMPAR---")
numero = int(input("Escribe un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es PAR\n")
else:
    print(f"El número {numero} es IMPAR\n") 

# 2. Determinar si un número es positivo o negativo.
print("\n---Ej2. POSITIVO O NEGATIVO---")
numero = int(input("Escribe un número: "))
if numero > 0:
    print("El número es positivo\n")
elif numero == 0:
    print("El número es neutro\n")
else:
    print("El número es negativo\n")

# 3. Comprobar si una persona es mayor o menor de edad.
print("\n---Ej3. MAYOR O MENOR DE EDAD---")
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad\n")
elif edad <= 0:
    print("Error, no hay edades negativas")
else:
    print("Eres menor de edad\n")

# 4. Evaluar si un estudiante aprueba una materia.
print("\n---Ej4. APROBACIÓN DE MATERIA---")
calif = int(input("Digita tu calificación(0-100): "))
if calif >= 60:
    print("Aprobado\n")
else:
    print("Reprobado\n")

# 5. Clasificar una calificación en letras (A, B, C, D o F).
print("\n---Ej5. CLASIFICACIÓN DE CALIFICACIÓN EN LETRAS---")
calif = int(input("Digita tu calificación(0-100): "))
if calif >= 90:
    print("Tu calificación es: A\n")
elif calif >= 80:
    print("Tu calificación es: B\n")
elif calif >= 70:
    print("Tu calificación es: C\n")
elif calif >=60:
    print("Tu calificación es: D\n")
else:
    print("Tu calificación es: F\n")

# 6. Determinar el estado del agua según la temperatura.
temperatura = int(input("Digita la temperatura en grados Celcius: "))
if temperatura < 0:
    print("La temperatura es Sólida\n")
elif temperatura > 100:
    print("La temperatura es Vapor\n")
else: 
    print("La temperatura es Líquida")
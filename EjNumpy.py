#Jueves 6 de Marzo de 2025
#Gomez Trejo Ezequiel

import numpy as np
from numpy import random 

# 1. Crea un array de 10 números aleatorios enteros entre 0 y 100.
print("\n1. ARRAY ALEATORIO ENTEROS")
numeros = random.randint(0, 100, size=10)
print(numeros)

# 2. Crea un array de 5 números aleatorios decimales entre 0 y 1.

print("\n2. ARRAY ALEATORIO DECIMALES")
numeros_decimales = random.rand(5)
print(numeros_decimales)

# 3. Crea dos arrays de números aleatorios enteros de longitud 5 y concaténalos.
print("\n3. CONCATENAR ARRAYS")
array1 = random.randint(0, 100, size=5)
array2 = random.randint(0, 100, size=5)
print(f"Array 1: {array1}\n")
print(f"Array 2: {array2}\n")
concatenado = np.concatenate((array1, array2))
print(concatenado)

# 4. Crea un array de 10 números aleatorios enteros y sepáralo en dos arrays de 5 elementos cada uno.

print("\n4. SEPARAR ARRAYS")
array = random.randint(0, 10, size=10)
print(f"Array original: {array}\n")
array_separado = np.split(array, 2)
print(f"Array separado: {array_separado}\n")

# 5. Crea una matriz de 3x3 con números aleatorios decimales entre 0 y 1.
print("\n5. MATRIZ 3X3 ALEATORIA DECIMALES")
matriz = random.rand(3, 3)
print(matriz)

# 6. Crea un array de 10 números aleatorios enteros y selecciona 3 elementos al azar.
print("\n 6. SELECCIÓN DE 3 ELEMENTOS DEL ARRAY")
array = random.randint(1, 20, size=10)
print(f"Array: {array}\n")
print("Elementos seleccionados: ")
for i in range(3):
    seleccionado = random.choice(array)
    print(seleccionado)

# 7. Crea un array de 10 números aleatorios enteros entre 0 y 100 y calcula la media.
print("\n 7. MEDIA DE ARRAY NÚMEROS ALEATORIOS ENTRE 0 Y 100")
array = random.randint(1, 100, size=10)
print(f"Array: {array}")
media = np.mean(array)
print(f"\nMedia del array: {media}")
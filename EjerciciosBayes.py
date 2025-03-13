# Jueves 13 de marzo de 2025
# Gomez Trejo Ezequiel

import pandas as pd

# Ejercicio 1: Clasificación de frutas (Una característica)
print("\n------------------Ejercicio 1: Clasificación de frutas-----------------------\n")

# Paso 0: Creación de un DF
data = {
    'Fruta': ['Manzana', 'Pera'],
    'P(Fruta)': [0.6, 0.4],
    'P(Fruta|Roja)': [0.7, 0.2]
}

df = pd.DataFrame(data)
print(df)

# Paso 1: Probabilidad a priori P(c)
prob_manzana = df.loc[0, 'P(Fruta)']
prob_pera = df.loc[1, 'P(Fruta)']
print(f"\nP(Manzana) = {prob_manzana:.2f}")
print(f"P(Pera) = {prob_pera:.2f}\n")

# Paso 2: Probabilidad a condicionales P(c|x)
prob_manzana_roja = df.loc[0, 'P(Fruta|Roja)']
prob_pera_roja = df.loc[1, 'P(Fruta|Roja)']
print(f"P(Roja|Manzana) = {prob_manzana_roja:.2f}")
print(f"P(Roja|Pera) = {prob_pera_roja:.2f}\n")

# Paso 3: Aplicar el Teorema de Bayes
# Probabilidad de que sea fruta roja
fruta_roja = prob_manzana * prob_manzana_roja + prob_pera * prob_pera_roja
print(f"P(Fruta|Roja) = {fruta_roja:.2f}")

prob_manzana_red = (prob_manzana_roja * prob_manzana) / fruta_roja
print(f"\nLa probabilidad de que sea una Manzana dado que es Roja es: {prob_manzana_red:.2f}")

if prob_manzana_red > prob_pera_roja:
    print("\nLa fruta más probable es una Manzana roja.\n")
else:
    print("\nLa fruta más probable es una Pera roja.\n")



# Ejercicio 2: Detección de correo spam (Tres características)
print("\n------------------Ejercicio 2: Detección de correo spam-----------------------\n")

# Paso 0: Creación del DF
datos = {
    'Correo': ['Spam', 'Normal'],
    'Probabilidad': [0.3, 0.7],
    'Oferta': [0.9, 0.2],
    'Archivo': [0.8, 0.4],
    'Link': [0.85, 0.1]
}

df = pd.DataFrame(datos)
print(df)

# Paso 1: Probabilidades a priori P(c)
prob_spam = df.loc[0, 'Probabilidad']
prob_normal = df.loc[1, 'Probabilidad']
print(f"\nP(Spam) = {prob_spam:.2f}")
print(f"P(Normal) = {prob_normal:.2f}\n")

# Paso 2: Probabilidades Condicionales P(c|x)
# Probabilidad de que Correo Spam tenga oferta, archivo y link
spam_oferta = df.loc[0, 'Oferta']
spam_archivo = df.loc[0, 'Archivo']
spam_link = df.loc[0, 'Link']
spam_total = spam_oferta * spam_archivo * spam_link
print(f"P(c|s) = {spam_total:.4f}")

# Probabilidad de que Correo Normal tenga oferta, archivo y link
normal_oferta = df.loc[1, 'Oferta']
normal_archivo = df.loc[1, 'Archivo']
normal_link = df.loc[1, 'Link']
normal_total = normal_oferta * normal_archivo * normal_link
print(f"P(c|N) = {normal_total:.4f}")

prob_spam_total = prob_spam * spam_total
prob_normal_total = prob_normal * normal_total
print(f"\nP(S|T) = {prob_spam_total:.4f}")
print(f"P(N|T) = {prob_normal_total:.4f}")

# Paso 3: Teorema de Bayes
# Calculo de P(c)
prob_todos = prob_spam_total + prob_normal_total
print(f"P(c) = {prob_todos:.4f}")

prob_spam_todos = (spam_total * prob_spam) / prob_todos
print(f"\nP(Spam|Oferta, Archivo y Link) = {prob_spam_todos:.4f}\n")

if prob_spam_todos > prob_normal_total:
    print("El correo es más probablemente Spam.\n")
else:
    print("El correo es más probablemente Normal.\n")
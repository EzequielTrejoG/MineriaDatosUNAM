#Jueves 20-03-2025
#Gomez Trejo Ezequiel

import numpy as np
from scipy import stats

#Ejercicio 1-----------------------------------------------------------------------------------------------------------------------------------

# Configurar semilla para reproducibilidad
np.random.seed(42)

# Parámetros de la distribución normal
media_poblacional = 45
tamaño_muestra = 25
s = 10

# Generar muestra aleatoria
muestra = np.random.normal(media_poblacional, s, tamaño_muestra)

# Prueba T de una muestra
t_stat, p_value = stats.ttest_1samp(muestra, 45)

# Resultados
print("\n-----------------------Ejercicio 1. PRUEBA T DE UNA MUESTRA (EMPRESA TECNOLÓGICA)------------------------------------------------------\n")
print(f"Muestra: \n{muestra}\n")
print(f"\nMedia poblacional: {media_poblacional}\nTamaño de la muestra: {tamaño_muestra}\nDesviación estándar: {s}")
print(f"\nEstadístico t: {t_stat:.4f}\nValor p: {p_value:.4f}\n")

# Interpretación con nivel de significancia 0.05
alpha = 0.05
if p_value < alpha:
    print("Rechazamos la hipótesis nula (H0. El tiempo promedio es significativamente diferente de 45 minutos.")
else:
    print("No hay evidencia suficiente para rechazar la hipótesis nula (H0).\n")

#Ejercicio 2-----------------------------------------------------------------------------------------------------------------------------------
# Configurar semilla para reproducibilidad
np.random.seed(42)

# Parámetros de la distribución normal
muestra = 30
grupoA = int(muestra / 2)
grupoB = int(muestra / 2)
mediaA = 3.5
desvA = 1.2
mediaB = 4.5
desvB = 1.5

# Generar dos muestras aleatorias
muestraA = np.random.normal(mediaA, desvA, grupoA)
muestraB = np.random.normal(mediaB, desvB, grupoB)

# Prueba T de dos muestras independientes
t_stat, p_value = stats.ttest_ind(muestraA, muestraB)

# Resultados
print("\n-----------------------------Ejercicio 2. PRUEBA T DE MUESTRAS INDEPENDIENTES (GIMNASIO)----------------------------------------------\n")
print(f"A. Entrenamiento Tradicional: \n{muestraA}\n")
print(f"B. Entrenamiento de Alta Intensidad: \n{muestraB}\n")
print(f"\nMedia poblacional A: {mediaA}\nTamaño de la muestra: {grupoA}\nDesviación estándar A: {desvA}")
print(f"\nMedia poblacional B: {mediaB}\nTamaño de la muestra: {grupoB}\nDesviación estándar B: {desvB}\n")
print(f"\nEstadístico t: {t_stat:.4f}\nValor p: {p_value:.4f}\n")

# Interpretar el resultado de la Prueba T
if p_value < 0.05:
    print("Rechazamos la hipótesis nula (H0). Los promedios de las dos muestras son significativamente diferentes.\n")
else:
    print("No hay evidencia suficiente para rechazar la hipótesis nula (H0).\n")

#Ejercicio 3 -------------------------------------------------------------------------------------------------------------------------
#Datos de niveles de colesterol antes y después de la dieta
antes = np.array([150, 160, 170, 180, 190, 200, 155, 165, 175, 185, 195, 205, 145, 112, 185, 120, 100, 143, 147, 150])
despues = np.array([145, 155, 165, 175, 185, 195, 150, 160, 170, 180, 190, 200, 140, 105, 160, 110, 95, 120, 100, 134])

# Prueba T Pareada
t_stat, p_value = stats.ttest_rel(antes, despues)

# Resultados
print("\n-----------Ejercicio 3. PRUEBA T DE MUESTRAS DEPENDIENTES - Niveles de colesterol antes y después de la dieta---------------------------\n")
print(f"Antes: \n{antes}\n")
print(f"Después: \n{despues}\n")
print(f"\nEstadístico t: {t_stat:.4f}\nValor p: {p_value:.4f}\n")

# Interpretación del resultado
if p_value < 0.05:
    print("Rechazamos la hipótesis nula (H0). Los niveles de colesterol antes y después de la dieta son significativamente diferentes.\n")
else:
    print("No hay evidencia suficiente para rechazar la hipótesis nula (H0).\n")

#Ejercicio 4 -------------------------------------------------------------------------------------------------------------------------
#Velocidad de reacción de jóvenes(18-30 años) y adultos mayores(60+ años)
jovenes = np.array([324, 293, 332, 376, 288, 288, 378, 338, 276, 327, 276, 276, 312, 204, 213, 271, 249, 315, 254, 229])
adultos = np.array([552, 434, 454, 350, 411, 457, 369, 476, 407, 429, 407, 579, 449, 375, 507, 364, 464, 312, 357, 463])

# Prueba T de dos muestras independientes
t_stat, p_value = stats.ttest_ind(jovenes, adultos)

# Resultados
print("\n--------------------Ejercicio 4. PRUEBA T DE MUESTRAS INDEPENDENTES -- Velocidad de reacción de jóvenes y adultos mayores---------------\n")
print(f"Jovenes: \n{jovenes}\n")
print(f"Adultos: \n{adultos}\n")
print(f"\nEstadístico t: {t_stat:.4f}\nValor p: {p_value:.4f}\n")

# Interpretación del resultado
if p_value < 0.05:
    print("Rechazamos la hipótesis nula (H0). La velocidad de reacción de jóvenes y adultos mayores es significativamente diferente.\n")
else:
    print("No hay evidencia suficiente para afirmar que existe una diferencia significativa.\n")
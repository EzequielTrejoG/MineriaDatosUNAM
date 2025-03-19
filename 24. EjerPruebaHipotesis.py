# Miércoles 19-0-2025

import pandas as pd
import numpy as np
import scipy.stats as stats

# PROBLEMA 1-----------------------------------------------------------------------------------------------------------------------------
# Datos
hipo_nula = 10
n = 49
promedio = 9.7
desv = 0.5
alpha = 0.01

# Cálculo del estadístico de prueba Z
z = (promedio - hipo_nula) / (desv/np.sqrt(n))

#Valor critico para la prueba 
z_critical = stats.norm.ppf(1-alpha)

print("\n----------Problema 1: Control de Calidad en una Fábrica de Tornillos----------\n")
#Crear un DataFrame con los datos
df = pd.DataFrame({
    'Parámetros': ['Hipótesis Alternativa', 'Media poblacional', 'Media muestral', 'Desviacion estandar', 'Tamaño de muestra', 'Nivel Significancia', 'Z-calculado', 'Z-crítico', 'Conclusión' ],
    'Valores': ['H1 < 10', hipo_nula, promedio, desv, n, alpha, z, z_critical, 'Rechazar la hipótesis nula' if z < z_critical else 'No rechazar la hipótesis nula']
})

print(df)

# PROBLEMA 2-----------------------------------------------------------------------------------------------------------------------------
# Datos
media_poblacional = 20
n = 30
media_muestra = 18.5
s = 2.5
alpha = 0.05

# Cálculo del estadístico de prueba Z
z = (media_muestra - media_poblacional) / (s/np.sqrt(n))

# Valor critico para la prueba
z_critical = stats.norm.ppf(1-alpha)

print("\n----------Problema 2: Duración de Baterías de Celulares----------\n")
df = pd.DataFrame({
    'Parámetros': ['Hipótesis Alternativa', 'Media poblacional', 'Media muestral', 'Desviación estandar', 'Tamaño de muestra', 'Nivel Significancia', 'Z-calculado', 'Z-crítico',  'Conclusión' ],
    'Valores': ['H1 < 20', media_poblacional, media_muestra, s, n, alpha, z, z_critical,'Rechazar la hipótesis nula' if z < z_critical else 'No rechazar la hipótesis nula']
})

print(df)

# PROBLEMA 3-----------------------------------------------------------------------------------------------------------------------------
# Datos
H0 = 1000
n = 40
x_muestra = 990
s_muestra = 12
alpha = 0.02

# Cálculo de Z
z = (x_muestra - H0)/(s_muestra/np.sqrt(n))

# Valor crítico para la prueba
z_critica = stats.norm.ppf(1-alpha)

print("\n----------Problema 3: Control de Peso en una Planta de Alimentos----------\n")
df = pd.DataFrame({
    'Parámetros': ['Hipótesis Alternativa', 'Media Poblacional', 'Media Muestral', 'Desviación Estándar', 'Tamaño de muestra', 'Nivel Significancia', 'Z-Calculado', 'Z-Crítico', 'Conclusión'],
    'Valores': ['H1 < 1000', H0, x_muestra, s_muestra, n, alpha, z, z_critica, 'Rechazar la hipótesis nula' if z < z_critica else 'No rechazar la hipótesis nula']
})

print(df)
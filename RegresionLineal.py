#Sábado 29 de Marzo de 2025
#Gomez Trejo Ezequiel

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from tabulate import tabulate
from scipy import stats

#===========================================================================================================
#Ejercicio 1
#===========================================================================================================

#1. Carga del dataset y exploración
datos = pd.read_csv('PublicidadVentas.csv')

# Exploración
print("\n----- ANÁLISIS DE PUBLICIDAD DIGITAL vs VENTAS -----\n")
print("Primeras 5 líneas del Dataset:")
print(datos.head())
print("\nEstadísticas descriptivas:")
print(datos.describe().round(2))
print("\nInformación del Dataset:")
print(datos.info())

#2. Preparación de datos
x = datos[['Inversion']].values
y = datos['Ventas'].values

# División de datos
x_train, x_test, y_train, y_test = train_test_split(
    x, y, 
    test_size=0.2,
    random_state=42
)

#3. Creación y Entrenamiento del modelo
modelo = LinearRegression()
modelo.fit(x_train, y_train)

#4. Evaluación del modelo
y_pred = modelo.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

#Imprimir evaluación del modelo
print("\nEVALUACIÓN DEL MODELO:")
pendiente = f"{modelo.coef_[0]:.2f}"
intercepto = f"{modelo.intercept_:.2f}"
mse_modelo = f"{mse:.2f}"
r2_modelo = f"{r2:.2f}"
ecuacion_modelo = f"y = {modelo.coef_[0]:.2f}x + {modelo.intercept_:.2f}"

df = pd.DataFrame({
    'Descripción': ['Pendiente', 'Intercepto', 'MSE', 'R2', 'Ecuación'],
    'Valor': [pendiente, intercepto, mse_modelo, r2_modelo, ecuacion_modelo]
})

print(df)

#5. Visualización
plt.figure(figsize=(12, 6))
plt.scatter(x, y, color='blue', label='Datos reales')
plt.xlabel('Inversión en Publicidad (miles de $)', fontsize=12)
plt.ylabel('Unidades Vendidas', fontsize=12)
plt.plot(x, modelo.predict(x), color='red', linewidth=2, label='Regresión Lineal')
#Ecuación
ecuacion = f'y = {modelo.coef_[0]:.2f}x + {modelo.intercept_:.2f}'
#plt.text(0.5, 1400, ecuacion, fontsize=12)
plt.text(min(x), max(y), ecuacion, fontsize=12, color='black', verticalalignment='top')
plt.title('Relación entre Inversión en Publicidad y Ventas\n', fontsize=14)
plt.legend()
plt.show()

# 6. Predicción
print("\nPREDICCIONES DE VENTAS:")
inversiones = np.array([[1.0], [1.5], [5.0], [10.0], [15.0], [20.0]])
datos = []
for inversion in inversiones:
    prediccion = modelo.predict(inversion.reshape(-1, 1))
    datos.append([inversion[0], f"{prediccion[0]:.2f}"])
tabla = tabulate(datos, headers=['Inversión (k)', 'Unidades'], tablefmt='pretty')
print(tabla)

#===========================================================================================================
#Ejercicio 2
#===========================================================================================================

#1. Carga del dataset y exploración
datos = pd.read_csv('EdadSeguros.csv')

# Exploración
print("\n----- ASEGURADORA -----\n")
print("Primeras 5 líneas del Dataset:")
print(datos.head())
print("\nEstadísticas descriptivas:")
print(datos.describe().round(2))
print("\nInformación del Dataset:")
print(datos.info())

#2. Preparación de datos
x = datos[['Edad']].values
y = datos['Costo'].values

# División de datos
x_train, x_test, y_train, y_test = train_test_split(
    x, y, 
    test_size=0.2,
    random_state=42
)

#3. Creación y Entrenamiento del modelo
modelo = LinearRegression()
modelo.fit(x_train, y_train)

#4. Evaluación del modelo
y_pred = modelo.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

#Imprimir evaluación del modelo
print("\nEVALUACIÓN DEL MODELO:")
pendiente = f"{modelo.coef_[0]:.2f}"
intercepto = f"{modelo.intercept_:.2f}"
mse_modelo = f"{mse:.2f}"
r2_modelo = f"{r2:.2f}"
ecuacion_modelo = f"y = {modelo.coef_[0]:.2f}x + {modelo.intercept_:.2f}"

df = pd.DataFrame({
    'Descripción': ['Pendiente', 'Intercepto', 'MSE', 'R2', 'Ecuación'],
    'Valor': [pendiente, intercepto, mse_modelo, r2_modelo, ecuacion_modelo]
})

print(df)

#5. Cálculo de intervalos de confianza
x_plot = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
y_plot = modelo.predict(x_plot)

# Calcular residuos y grados de libertad
residuos = y_train - modelo.predict(x_train)
grados_libertad = len(x_train) - 2

# Valor t para 95% de confianza
t_valor = stats.t.ppf(0.975, grados_libertad)

# Error estándar de los residuos
error_estandar = np.sqrt(np.sum(residuos**2) / grados_libertad)

# Calcular intervalos de confianza
X_train_mean = x_train.mean()
suma_cuadrados = np.sum((x_train - X_train_mean)**2)

intervalos_confianza = t_valor * error_estandar * np.sqrt(
    1/len(x_train) + (x_plot - X_train_mean)**2 / suma_cuadrados
)

#6. Visualización
plt.figure(figsize=(12, 6))
plt.scatter(x, y, color='blue', alpha=0.6, label='Datos reales')
plt.plot(x_plot, y_plot, color='red', linewidth=2, label='Regresión Lineal')

# Área de intervalo de confianza
plt.fill_between(
    x_plot.ravel(), 
    y_plot - intervalos_confianza.ravel(), 
    y_plot + intervalos_confianza.ravel(),
    color='orange', alpha=0.3, label='IC 95%'
)

#Ecuación
ecuacion = f'y = {modelo.coef_[0]:.2f}x + {modelo.intercept_:.2f}'
plt.text(min(x), max(y), ecuacion, fontsize=12, color='black', verticalalignment='top')
plt.title('ASEGURADORA', fontsize=14)
plt.xlabel('Edad', fontsize=12)
plt.ylabel('Costo', fontsize=12)
plt.legend()
plt.show()

# 7. Predicción
print("\nPREDICCIONES DE COSTOS DE ACUERDO A LA EDAD:")
edades = np.array([[30], [40], [50], [60]])
datos = []
for edad in edades:
    prediccion = modelo.predict(edad.reshape(-1, 1))
    # Calcular intervalo de confianza para cada predicción
    ic = t_valor * error_estandar * np.sqrt(
        1/len(x_train) + (edad - X_train_mean)**2 / suma_cuadrados
    )
    datos.append([
        edad[0], 
        f"{prediccion[0]:.2f}", 
        f"{prediccion[0] - ic[0]:.2f} - {prediccion[0] + ic[0]:.2f}"
    ])
    
tabla = tabulate(
    datos, 
    headers=['Edad', 'Costo', 'Intervalo 95% Confianza'], 
    tablefmt='pretty'
)
print(tabla)

#===========================================================================================================
#Ejercicio 3
#===========================================================================================================

#1. Carga del dataset y exploración
datos = pd.read_csv('PracticaExamenes.csv')

#Exploración
print("\n-----CALIFICACIONES DE EXÁMEN-----\n")
print(f"\nPrimeras 5 líneas del Dataset: \n {datos.head()}")
print(f"\n\nEstadística de los datos: \n {datos.describe()}")
print(f"\n\nInformación del Dataset: \n {datos.info()}")

#2. Preparación de datos
x = datos[['horas']].values
y = datos['puntuacion'].values

# División de datos
x_train, x_test, y_train, y_test = train_test_split(
    x, y, 
    test_size=0.2,
    random_state=42
)

#3. Creación y Entrenamiento del modelo
modelo = LinearRegression()
modelo.fit(x_train, y_train)

#4. Evaluación del modelo
y_pred = modelo.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

#Imprimir evaluación del modelo
print("\nEVALUACIÓN DEL MODELO:")
print("\nEVALUACIÓN DEL MODELO:")
pendiente = f"{modelo.coef_[0]:.2f}"
intercepto = f"{modelo.intercept_:.2f}"
mse_modelo = f"{mse:.2f}"
r2_modelo = f"{r2:.2f}"
ecuacion_modelo = f"y = {modelo.coef_[0]:.2f}x + {modelo.intercept_:.2f}"

df = pd.DataFrame({
    'Descripción': ['Pendiente', 'Intercepto', 'MSE', 'R2', 'Ecuación'],
    'Valor': [pendiente, intercepto, mse_modelo, r2_modelo, ecuacion_modelo]
})

print(df)

#5. Visualización
plt.figure(figsize=(12, 6))
plt.scatter(x, y, color='blue', label='Datos Reales')
plt.xlabel('Horas', fontsize=14)
plt.ylabel('Calificación', fontsize=12)
plt.plot(x, modelo.predict(x), color='red', linewidth=2, label='Regresión Lineal')

# Ecuación de la recta
ecuacion = f'y = {modelo.coef_[0]:.2f}x + {modelo.intercept_:.2f}'
plt.text(min(x), max(y), ecuacion, fontsize=12, color='black', verticalalignment='top')
plt.text(1, 10, ecuacion, fontsize=12)

plt.title('Calificación según las horas de práctica')
plt.legend()
plt.show()

#6. Predicción
print("\nPREDICCIONES DE CALIFICACIONES DE EXÁMEN")
horas_estudio = np.array([[30], [40], [50], [60]])
datos = []
for horas in horas_estudio:
    prediccion = modelo.predict(horas.reshape(-1, 1))
    datos.append([horas[0], f"{prediccion[0]:.2f}"])
tabla = tabulate(datos, headers=["Horas de práctica", "Calificación"], tablefmt="pretty")
print(tabla)
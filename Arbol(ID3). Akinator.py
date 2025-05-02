# Viernes 2 de Mayo de 2025
# Gomez Trejo Ezequiel

#--------------------------------------------------------------------------------------------------------------------------------------------
# Árbol de Decisión. Algoritmo ID3. AKINATOR
#--------------------------------------------------------------------------------------------------------------------------------------------

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# 1. Dataset de personajes (Categórico)
data = {
    'Nombre': ['Superman', 'Brad Pitt', 'Einstein', 'Harry Potter', 'Angelina Jolie', 'Sherlock Holmes'],
    'Real': ['No', 'Sí', 'Sí', 'No', 'Sí', 'No'],
    'Actor': ['No', 'Sí', 'No', 'No', 'Sí', 'No'],
    'Poderes': ['Sí', 'No', 'No', 'Sí', 'No', 'No'],
    'Clase': ['Superhéroe', 'Actor', 'Científico', 'Mago', 'Actriz', 'Ficción']
}

df = pd.DataFrame(data)
print("\nDataFrame:\n")
print(df)

# 2. Codificación de Variables Categóricas a numéricas
le = LabelEncoder()
df_encoded = df.copy()
for columna in ['Real', 'Actor', 'Poderes', 'Clase']:
    df_encoded[columna] = le.fit_transform(df[columna])

print("\nDataset codificado: \n")
print(df_encoded)

# 3. Separación de Características (x) y taget(y)
X = df_encoded.drop(['Nombre', 'Clase'], axis=1)
y = df_encoded['Clase']

# 4. Entrenamiento del Árbol de Decisión con ID3 (entropía)
modelo = DecisionTreeClassifier(
    criterion='entropy',
    max_depth=3,
    random_state=42
)
modelo.fit(X, y)

# 5. Visualización del Árbol de Decisión
plt.figure(figsize=(9, 5))
plot_tree(
    modelo, 
    feature_names = X.columns,
    class_names = df['Clase'].unique(),
    filled = True,
    rounded = True
)
plt.title('Árbol de Decisión - Akinator')
plt.show()

# 6. Función para jugar Akinator
def jugar_akinator(modelo, df):
    print("\n¡Bienvenido a Akinator!")
    print("\nPiensa en un personaje de la lista y responde las preguntas con 'Sí' o 'No' \n")
    personajes = df['Nombre'].tolist() # Lista de personajes .tolist() es una función de pandas que convierte una serie en una lista
    for personaje in personajes:
        print(personaje)

    #Inicializar respuestas
    respuestas = {}
    for feature in X.columns:
        respuesta = input(f"¿{feature}? (Sí/No): ").strip().lower() # .strip() elimina espacios en blanco y .lower convierte a minúsculas
        respuestas[feature] = 1 if respuesta == 'sí' else 0 #Convertir respuesta a 1 o 0

    #Predecir el personaje
    input_user = pd.DataFrame([respuestas]) # Crear un DataFrame con las respuestas del usuario
    prediccion = modelo.predict(input_user) # Predice la clase del personaje
    clase_predicha = le.inverse_transform(prediccion)[0] # Invierte la codificación para obtener la clase original
    nombre_predicho = df[df['Clase'] == clase_predicha]['Nombre'].values[0] #Obtiene el nombre del personaje predicho
    print(f"\nTu personaje es: {nombre_predicho} ({clase_predicha})!")

#Ejecutar el juego
jugar_akinator(modelo, df)
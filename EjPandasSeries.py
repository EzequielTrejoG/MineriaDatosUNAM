#Martes 25 de Febrero de 2025

import pandas as pd
import random

# 1. Registro de temperaturas: Se necesita crear un registro que contenga las temperaturas promedio de una ciudad durante 7 días. 
# La serie debe incluir los días de la semana como índice y las temperaturas como valores. 
# Luego, calcula la temperatura promedio de la semana.
class Temperatura:
    
    def __init__(self, lun, mar, mier, jue, vier, sab, dom):
        self.temperaturas =  {'Lunes': lun, 'Martes': mar, 'Miércoles': mier, 'Jueves': jue, 'Viernes': vier, 'Sábado': sab, 'Domingo': dom}
        self.serieTemperaturas = pd.Series(self.temperaturas)
    
    def mostrarTemperaturas(self):
        print("\nLas temperaturas registradas son: ")
        print(self.serieTemperaturas)
    
    def promedioTemperaturas(self):
        promedio = self.serieTemperaturas.mean()
        print(f"\nEl promedio es de las temperaturas registradas es de: {promedio} ºC\n")

print("\n----TEMPERATURAS DEL ESTADO DE MÉXICO----")
print("\nRegistra las temperaturas que se regsitraron en la semana\n")
lun = float(input("Lunes: "))
mar = float(input("Martes: "))
mier = float(input("Miércoles: "))
jue = float(input("Jueves: "))
vie = float(input("Viernes: "))
sab = float(input("Sábado: "))
dom = float(input("Domingo: "))

temp = Temperatura(lun, mar, mier, jue, vie, sab, dom)
temp.mostrarTemperaturas()
temp.promedioTemperaturas()

# 2. Inventario de productos: Crea una serie que represente el inventario de una tienda, donde el índice sea 
# el nombre del producto y los valores sean la cantidad disponible en stock. Luego, filtra los productos 
# que tienen menos de 10 unidades en stock.

# Inventario de productos
class Producto():

    def __init__(self):
        self.productos = {'Galletas': 10, 'Refrescos': 56, 'Jabón': 5, 'Cepillos': 3, 'Agua': 9, 'Jugo': 17}
        self.serieProductos = pd.Series(self.productos)
    
    def productosMayor(self):
        filtro = self.serieProductos[self.serieProductos < 10]
        print("\n----TIENDA DE LA ESQUINA----")
        print(f"\nLos productos con menos de 10 unidades son: \n\n{filtro}\n")

productos = Producto()
productos.productosMayor()

# 3. Precios de productos: Genera una serie que contenga los precios de 5 productos diferentes. 
# Luego, aplica un descuento del 15% a cada producto y muestra la serie actualizada.
class precioProductos:

    def __init__(self):
        self.productos = {'Takis': 25, 'Jugo': 18, 'Tomate': 64, 'Jamón': 108, 'Galletas': 14}
        self.serieProductos = pd.Series(self.productos) 
    
    def mostrarProductos(self):
        print("\n----EL OCZO----")
        print(f"\nPrecios de los productos: \n\n{self.serieProductos}\n")

    def hacerDescuento(self):
        productos = self.serieProductos
        descuento = productos * 0.85
        print(f"El precio de los productos con 15% de descuento es: \n\n {descuento}\n")

productos = precioProductos()
productos.mostrarProductos()
productos.hacerDescuento()

# 4. Calificaciones de estudiantes: Crea una serie que almacene las calificaciones de 10 estudiantes en un examen. 
# El índice debe ser el nombre del estudiante. Encuentra la calificación más alta y la más baja.
class Calificaciones:

    def __init__(self):
        self.nombres = ['Cinthia', 'Maria', 'Fernanda', 'Ángel', 'Sarahi', 'Erick', 'Berenice', 'Angelica', 'Yolanda', 'Dennis']
        self.calificaciones = [9, 7, 10, 10, 6, 8, 5, 5, 10, 9]
        self.serie = pd.Series(self.calificaciones, index=self.nombres)
    
    def mostrarCalifMinMax(self):
        califMin = self.serie.min()
        califMax = self.serie.max()
        print("\n---Calificaciones---")
        print(self.serie)
        print(f"\nLa calificación más alta es de: {califMax}")
        print(f"\nLa calificación más baja es de: {califMin}")

calif = Calificaciones()
calif.mostrarCalifMinMax()

# 5. Registro de ventas: Genera una serie que represente las ventas diarias de una tienda durante 5 días. 
# Luego, calcula el total de ventas de la semana y el día con mayores ventas.
class Ventas:

    def __init__(self, ventas):
        self.dias = ['Día 1', 'Día 2', 'Día 3', 'Día 4', 'Día 5']
        self.ventas = pd.Series(ventas, index=self.dias)

    def mostrarVentas(self):
        print(f"\nLas ventas registrada en estos cinco días son: \n{self.ventas}")
    
    def calcularTotalVentas(self):
        totalVentas = self.ventas.sum()
        print(f"\nLa ventas totales son de $: {totalVentas} pesos")
    
    def mayorVentas(self):
        dia = self.ventas.idxmax()
        cantidad = self.ventas.max()
        print(f"El día que se obtuvo mayor ventas es en el {dia} con un total de $200{cantidad}\n")

print("\n----REGISTRO DE VENTAS----")
ventas = []
for i in range(5):
    venta = float(input(f"Día {i+1}: "))
    ventas.append(venta)

ventas = Ventas(ventas)
ventas.mostrarVentas()
ventas.calcularTotalVentas()
ventas.mayorVentas()

# 6. Comparación de precios: Crea dos series que representen los precios de los mismos productos en dos tiendas diferentes. 
# Compara las series para identificar en qué tienda los productos son más baratos.
class comparaPrecios:
    def __init__(self):
        self.tienda1 = {'Agua': 12, 'Pan': 3, 'Pepsi': 23, 'Jarrito': 18, 'Donas': 26, 'Jamón': 35}
        self.tienda2 = {'Agua': 10, 'Pan': 2, 'Pepsi': 25, 'Jarrito': 15, 'Donas': 29, 'Jamón': 35}
    
    def compararPrecios(self):
        print("\n-----TIENDA DE LA ESQUINA VS TIENDA OCZO-----")
        print("\nProducto\tTienda Esquina\tTienda Oczo\tMás barata")
        print("-------------------------------------------------------------")
        for producto in self.tienda1:
            precio1 = self.tienda1[producto]
            precio2 = self.tienda2[producto]

            if precio1 < precio2:
                mas_barata = "Tienda Esquina"
            elif precio1 > precio2:
                mas_barata = "Tienda Oczo"
            else:
                mas_barata = "Precios iguales"

            print(f"{producto}\t\t${precio1}\t\t${precio2}\t\t{mas_barata}")

tiendas = comparaPrecios()
tiendas.compararPrecios()

# 7. Suma de series: Genera dos series que representen los ingresos y gastos diarios de una empresa durante 5 días. 
# Luego, crea una tercera serie que muestre el beneficio diario (ingresos - gastos).
class Empresa:
    def __init__(self, ingresos, gastos):
        self.dias = ['Día 1', 'Día 2', 'Día 3', 'Día 4', 'Día 5']
        self.ingresos = pd.Series(ingresos, index=self.dias)
        self.gastos = pd.Series(gastos, index=self.dias) 
    
    def mostrarBeneficioDiario(self):
        beneficio = self.ingresos - self.gastos 
        print("\n---Las utilidades de la Empresa Patito S.A de C.V son: ---\n")
        print(beneficio)

        print("\n-----BENEFICIO DIARIO DETALLADO-----")
        print(f"\nDía\t\tIngresos\tGastos\t\tBeneficio")
        for i in range(5):
            dia = self.dias[i]
            print(f"{dia}\t\t${self.ingresos[dia]}\t\t${self.gastos[dia]}\t\t${beneficio[dia]}")

# Entrada de datos
print("\n------EMPRESA PATITO------")
print("\nRegistra tus ingresos: ")
ingresos = [float(input(f"Ingreso del día {i+1}: ")) for i in range(5)]

print("\nRegistra tus gastos: ")
gastos = [float(input(f"Gasto del día {i+1}: ")) for i in range(5)]

# Crear la empresa y mostrar el beneficio diario
empresa = Empresa(ingresos, gastos)
empresa.mostrarBeneficioDiario()

# 8. Filtrado de datos: Crea una serie que contenga las edades de 15 personas. 
# Filtra la serie para mostrar solo las edades mayores a 18 años.
class Edades:

    def __init__(self):
        self.datos = {'Ana': 40, 'Cinthia': 5, 'Fernanda': 13, 'Angel': 18, 'Pedro': 32, 'Angelica': 50, 'Dennis': 31, 'Berenice': 10,
            'Yolanda': 15, 'Erick': 3, 'Dorian': 8, 'Rivera': 65, 'Juan': 15, 'Salvador': 70, 'Sarahi': 7}
        self.serieDatos = pd.Series(self.datos)

    def mostrarDatos(self):
        print("\n---Edades---")
        print(f"\n{self.serieDatos}\n")
    
    def buscarMayores(self):
        mayores = self.serieDatos[self.serieDatos >= 18]
        print("\n---Personas que son mayores de edad---")
        print(f"\n{mayores}\n")

personas = Edades()
personas.mostrarDatos()
personas.buscarMayores()

# 9. Aplicación de funciones: Genera una serie que contenga los valores de 10 números aleatorios. 
# Aplica una función que eleve al cuadrado cada valor y muestra la serie resultante.
class Numeros:

    def __init__(self):
        self.numeros = [random.randint(1, 100) for _ in range(10)] 
        self.serieNumeros = pd.Series(self.numeros) 

    def elevarCuadrado(self):
        print("\n----------Los números generados son: \n")
        print(f"\n{self.serieNumeros}\n")
        cuadrados = self.serieNumeros ** 2
        print("El cuadrado de esos números es: ")
        for i in range(10):
            print(f"{self.serieNumeros[i]}^2 = {cuadrados[i]}")

numeros = Numeros()
numeros.elevarCuadrado()

# 10. Concatenación de series: Crea dos series que representen las ventas de meses diferentes. 
# Concatena las series para obtener un registro completo de ventas de los meses.
class Ventas:

    def __init__(self):
        self.meses1 = ['Enero', 'Febrero']
        self.ventames1 = [15000, 18900]
        self.meses2 = ['Marzo', 'Abril']
        self.ventames2 = [20000, 23000]
        self.serie1 = pd.Series(self.ventames1, index=self.meses1)
        self.serie2 = pd.Series(self.ventames2, index=self.meses2)
    
    def concatenarSeries(self):
        concatenar = pd.concat([self.serie1, self.serie2])
        print("\n-----VENTAS-----")
        print(concatenar)

ventas = Ventas()
ventas.concatenarSeries()
#Jueves 11 de Febrero de 2025
#Gomez Trejo Ezequiel

#CLASE COCHE-------------------------------------------------------------------------------------------------------
class Coche:

    def __init__(self, id, marca, modelo, color):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0
    
    def mostrarInformacion(self):
        print("\n---BUSCAR COCHE---")
        id = input("\nIngrese el id del coche: ")
        if id == self.id:
            print(f"\nID Coche: {self.id} \nMarca: {self.marca} \nModelo: {self.modelo} \nColor: {self.color} \nVelocidad: {self.velocidad}\n")
        else:
            print("Coche no encontrado")
    
    def aumentarVelocidad(self):
        print("\n---AUMENTAR VELOCIDAD---")
        id = input("\nEscribe el ID de su coche: ")
        if id == self.id:
            print(f"Actualmente su coche tiene una velocidad de {self.velocidad}")
            velocidad = float(input("\n¿Cuánta velocidad quiere aumentar?: "))
            if velocidad <= 0:
                print("La velocidad debe ser mayor a cero\n")
            else:
                self.velocidad += velocidad
                print(f"Ahora la velocidad de su coche es {self.velocidad}\n")
        else:
            print("Coche no encontrado\n")
    
    def disminuirVelocidad(self):
        print("\n---DISMINUIR VELOCIDAD---")
        id = input("\nEscribe el ID de su coche: ")
        if id == self.id:
            print(f"Actualmente su coche tiene una velocidad de {self.velocidad}")
            velocidad = float(input("\n¿Cuánta velocidad quiere bajar?: "))
            if velocidad <= 0: 
                print("La velocidad debe ser mayor a cero\n")
            else:
                if velocidad > self.velocidad:
                    print("La velocidad no puede reducirse más de su nivel actual.")
                elif velocidad == self.velocidad:
                    self.velocidad -= velocidad
                    print("Su coche se ha detenido\n")
                else:
                    self.velocidad -= velocidad
                    print(f"Ahora la velocidad de su coche es {self.velocidad}\n")
        else:
            print("Coche no encontrado\n")

#CLASE CTA BANCARIA-------------------------------------------------------------------------------------------------------
class ctaBancaria:

    def __init__(self, nocta, titular, saldo):
        self.nocta = nocta
        self.titular = titular
        self.saldo = saldo
    
    def depositarDinero(self):
        nocta = int(input("\nDigite su número de cuenta: "))
        if nocta == self.nocta:
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            print(f"Usted ha ingresado {cantidad} pesos")
            self.saldo += cantidad
            print(f"Ahora su saldo es de {self.saldo}")
        else:
            print("No. de Cuenta no encontrado\n")
    
    def retirarDinero(self):
        nocta = int(input("\nDigite su número de cuenta: "))
        if nocta == self.nocta:
            if self.saldo == 0:
                print("Usted no tiene saldo en su cuenta\n")
            else:
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                if cantidad > self.saldo:
                    print("La cantidad a retirar es mayor al saldo que tiene disponible")
                elif cantidad == self.saldo:
                    self.saldo -= cantidad
                    print("Ha retirado todo su dinero de su cuenta")
                else:
                    print(f"Usted a retirado {cantidad} pesos")
                    self.saldo -= cantidad
                    print(f"Ahora su saldo actual es de {self.saldo}")
        else:
            print("No. de Cuenta no encontrado\n")
    
    def consultarSaldo(self):
        nocta = int(input("\nDigite su número de cuenta: "))
        if nocta == self.nocta:
            print(f"Su saldo actual es de {self.saldo} pesos")
        else:
            print("No. de Cuenta no encontrado\n")

#CLASE RECTANGULO-------------------------------------------------------------------------------------------------------
class Rectangulo:

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def calcularArea(self):
        print("---ÁREA DEL RECTÁNGULO---")
        area = self.ancho * self.alto
        print(f"El área del rectángulo es de {area}")
    
    def calcularPerimetro(self):
        print("---PERÍMETRO DEL RECTÁNGULO---")
        perimetro = (2 * self.ancho) + (2 * self.alto)
        print(f"El perímetro del rectángulo es de {perimetro}")
    
    def mostrarInformacion(self):
        print("---RECTÁNGULO---")
        area = self.ancho * self.alto
        perimetro = (2 * self.ancho) + (2 * self.alto)
        print(f"\nAncho: {self.ancho} \nAlto: {self.alto} \nÁrea: {area} \nPerímetro: {perimetro}")
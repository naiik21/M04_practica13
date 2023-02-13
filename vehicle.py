"""
Declaramos una obj llamado vehicle con sus 6 atributos ,
sus correspondientes getters y setters
y una funcion que nos devuelve su info
"""

class vehicle:
    def __init__(self, marca, modelo, color, motor, aspiracion, pais):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.aspiracion = aspiracion
        self.pais = pais

    def getmarca(self):
        return self.marca

    def setmarca(self, marca):
        self.marca = marca

    def getmodelo(self):
        return self.modelo

    def setmodelo(self, modelo):
        self.modelo = modelo

    def getcolor(self):
        return self.color

    def setcolor(self, color):
        self.color = color

    def getmotor(self):
        return self.motor

    def setmotor(self, motor):
        self.motor = motor

    def getaspiracion(self):
        return self.aspiracion

    def setaspiracion(self, aspiracion):
        self.aspiracion = aspiracion

    def getpais(self):
        return self.pais

    def setpais(self, pais):
        self.pais = pais

    def parts(self):
        print("La marca es: " + self.marca)
        print("El modelo: " + self.modelo)
        print("Su color es: " + self.color)
        print("Lleva un motor: " + self.motor)
        print("La aspiracion del coche es: " + self.aspiracion)
        print("El pais de fabricacion: " + self.pais + ".\n")
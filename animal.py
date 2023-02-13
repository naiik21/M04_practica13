"""
Declaramos una obj llamado animal con sus 6 atributos ,
sus correspondientes getters y setters
y una funcion que nos devuelve su info
"""

class animal:
    def __init__(self, raza, edad, color, sexo, alimentacion, habitat):
        self.raza = raza
        self.edad = edad
        self.color = color
        self.sexo = sexo
        self.alimentacion = alimentacion
        self.habitat = habitat

    def getraza(self):
        return self.raza

    def setraza(self, raza):
        self.raza = raza

    def getedad(self):
        return self.edad

    def setedad(self, edad):
        self.edad = edad

    def getcolor(self):
        return self.color

    def setcolor(self, color):
        self.color = color

    def getsexo(self):
        return self.sexo

    def setsexo(self, sexo):
        self.sexo = sexo

    def getalimentacion(self):
        return self.alimentacion

    def setalimentacion(self, alimentacion):
        self.alimentacion = alimentacion

    def gethabitat(self):
        return self.habitat

    def sethabitat(self, habitat):
        self.habitat = habitat

    def salutacio(self):
        print("La raza es: " + self.raza)
        print("Su edad: " + self.edad)
        print("Su color es: " + self.color)
        print("Su sexo: " + self.sexo)
        print("El animal es: " + self.alimentacion)
        print("su habitat suele ser: " + self.habitat + ".\n")

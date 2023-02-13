"""
Declaramos una obj llamado user con sus 6 atributos ,
sus correspondientes getters y setters
y una funcion que nos devuelve su info
"""
class user:
    def __init__(self, nom, cognom1, cognom2, correu, dni, edad):
        self.nom= nom
        self.cognom1 = cognom1
        self.cognom2 = cognom2
        self.correu = correu
        self.dni = dni
        self.edad = edad

    def getnom(self):
        return self.nom

    def setnom(self, nom):
        self.nom = nom

    def getcognom1(self):
        return self.cognom1

    def setcognom1(self, cognom1):
        self.cognom1 = cognom1

    def getcognom2(self):
        return self.cognom2

    def setcognom2(self, cognom2):
        self.cognom2 = cognom2

    def getcorreu(self):
        return self.correu

    def setcorreu(self, correu):
        self.correu = correu

    def getdni(self):
        return self.dni

    def setdni(self, dni):
        self.dni = dni

    def getedad(self):
        return self.edad

    def setedad(self, edad):
        self.edad = edad


    def salutacio(self):
        print("El nom del usuari es " + self.nom +" " + self.cognom1 + " " + self.cognom2 )
        print("amb dni " + self.dni + ", ")
        print("el seu correu es " + self.correu + " i ")
        print("la seva edat " + self.edad + ".\n")

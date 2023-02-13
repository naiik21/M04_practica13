"""
Declaramos una obj llamado university con sus 6 atributos ,
sus correspondientes getters y setters
y una funcion que nos devuelve su info
"""
class university:
    def __init__(self, nom, categoria, ciutat, pais, nEstudiants, nCarreres):
        self.nom= nom
        self.categoria = categoria
        self.ciutat = ciutat
        self.pais = pais
        self.nEstudiants = nEstudiants
        self.nCarreres = nCarreres

    def getnom(self):
        return self.nom

    def setnom(self, nom):
        self.nom = nom

    def getcategoria(self):
        return self.categoria

    def setcategoria(self, categoria):
        self.categoria = categoria

    def getciutat(self):
        return self.ciutat

    def setciutat(self, ciutat):
        self.ciutat = ciutat

    def getpais(self):
        return self.pais

    def setpais(self, pais):
        self.pais = pais

    def getnEstudiants(self):
        return self.nEstudiants

    def setnEstudiants(self, nEstudiants):
        self.nEstudiants = nEstudiants

    def getnCarreres(self):
        return self.nCarreres

    def setnCarreres(self, nCarreres):
        self.nCarreres = nCarreres


    def info(self):
        print("El nom l'universitat es " + self.nom)
        print("la seva educacio es " + self.categoria )
        print("esta situada en " + self.ciutat + ", " + self.pais + ".")
        print("Te un total de " + self.nEstudiants + " estudiants ")
        print("i " + self.nCarreres + " carreres.\n")

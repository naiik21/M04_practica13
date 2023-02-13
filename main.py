from book import book
from user import user
from university import university
import vehicle as vc
import animal as an
import school as sc

b1= book("El señor de los anillos", "J.r.r. Tolkien", "dura", "488", "Novela Fantastica", "MINOTAURO")
b2= book("El cuco de cristal", "Javier Castillo", "blanda", "488", "Novela", "SUMA")
us1= user("Nicolas", "Ratia", "Parejo", "nicolas.ratia@gmail.com", "47236073F", "20")
us2= user("Raul", "Llamas", "Molano", "raul.llamas@gmail.com", "47569573E", "19")
uni1= university("UAB", "publica", "Cerdanyola", "España", "3075", "47")
uni2= university("Gimbernat", "privada", "Sant Cugat", "España", "1209", "5")

v1 = vc.vehicle("Audi", "A3", "Azul", "2.0 TDI", "Turbo", "Alemania")
v2 = vc.vehicle("Honda", "Civic", "Blanco", "1.6 i-Vtec", "Natural", "Japon")
a1 = an.animal("Cerdo", "5 Años", "Rosa", "Macho", "Herbivoro", "Semitropicales")
a2 = an.animal("Caballo", "20 Años", "Marron", "Hembra", "Herbivoro", "Praderas")
s1 = sc.school("Jaume Balmes", "Barcelona", "España", "777", "Eso", "5")
s2 = sc.school("La guineueta", "Barcelona", "España", "1778", "Bachillerato", "4")



b1.info()
b2.info()
us1.salutacio()
us2.salutacio()
uni1.info()
uni2.info()

b1.setportada("blanda")
b2.setpagines("478")
us1.setedad("21")
us2.setdni("47456945R")
uni1.setnEstudiants("4075")
uni2.setnCarreres("7")

b1.info()
b2.info()
us1.salutacio()
us2.salutacio()
uni1.info()
uni2.info()


v1.parts()
v2.parts()
a1.salutacio()
a2.salutacio()
s1.info()
s2.info()

v1.setmarca("Aston Martin")
v2.setmodelo("Jazz")
a1.setedad("19")
a2.setcolor("Negro")
s1.setnEstudiantes("8453")
s2.setpais("Groenlandia")

v1.parts()
v2.parts()
a1.salutacio()
a2.salutacio()
s1.info()
s2.info()




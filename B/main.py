from book import book
from user import user
from university import university

b1= book("El señor de los anillos", "J.r.r. Tolkien", "dura", "488", "Novela Fantastica", "MINOTAURO")
b2= book("El cuco de cristal", "Javier Castillo", "blanda", "488", "Novela", "SUMA")
us1= user("Nicolas", "Ratia", "Parejo", "nicolas.ratia@gmail.com", "47236073F", "20")
us2= user("Raul", "Llamas", "Molano", "raul.llamas@gmail.com", "47569573E", "19")
uni1= university("UAB", "publica", "Cerdanyola", "España", "3075", "47")
uni2= university("Gimbernat", "privada", "Sant Cugat", "España", "1209", "5")

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

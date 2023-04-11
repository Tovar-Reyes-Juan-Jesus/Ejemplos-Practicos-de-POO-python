#CLASES Y METODOS,Objetos
#por Juan de jesus Tovar Reyes
#Mar 11 de abril 2023
class Coche():

    ruedas=4

    def desplazamiento(self):
        print("El coche se esta desplazando sobre 4 ruedas")

class Moto():

    ruedas=2

    def desplazamiento(self):
        print("La moto se esta desplazando sobre 2 ruedas")

miVehiculo=Coche()

print("Mi coche tiene ", miVehiculo.ruedas, " ruedas")

miVehiculo.desplazamiento()

print("---------------Segundo objeto---------------")

miVehiculo2=Moto()

print("Mi moto tiene ", miVehiculo2.ruedas, " ruedas")

miVehiculo2.desplazamiento()

#POLIMORFISMO

class Cachorro():

    def __init__(self, color, raza, id):
        self.color = color
        self.raza = raza
        self.id = id

    def __str__(self):
        return """\
Raza: {}
Color: {}""".format(self.raza, self.color)

    def __repr__(self) -> str:
        return "<Cachorro {}>".format(self.id)


perrito = Cachorro("Marrón claro", "Golden retriever", 1)
print(repr(perrito))

#ENCAPSULACION

class Ejemplo():

    def __init__(self):
        self.__oculto="Me encuentro oculto en la clase"

    def publico(self):
        return "Soy un método público, a la vista de todo"
    def __privado(self):
        print ("Soy un metodo privado, para ti no existo")
    def get_oculto(self):
        return self.__oculto
    def set_oculto(self):
        self.__oculto = self.__privado()

objeto = Ejemplo()

print(objeto.publico())

print(objeto._Ejemplo__privado())

print(objeto.get_oculto())

objeto.set_oculto()

#HERENCIA

class Padre():
  
    caballo="negro"
    ojos="azules"

    def conducir_coche(self):
        print ("La persona sabe conducir coches")

class Hijo(Padre):
  
    def conducir_moto(self):
        print ("La persona sabe conducir moto")

persona=Hijo()

print(persona.caballo)

print(persona.ojos)

persona.conducir_coche()

persona.conducir_moto() 




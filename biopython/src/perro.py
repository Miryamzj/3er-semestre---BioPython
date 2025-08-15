from random import choice

# CLASE MAMÍFERO
class Mamifero:
    vertebrado = True
    amamantan = True

    def __init__(self, alimentacion): 
        self.alimentacion = alimentacion
        self.progenie = 0 
        self.peso = 0
        self.altura = 0 

    def reproducirse(self, max_progenie):
        self.progenie = choice(range(max_progenie))

    def crecer(self, crecimiento):
        self.altura = crecimiento
        self.peso = crecimiento * 0.4 + self.peso  # usar self.peso, no 'peso'

# instancia de la clase 
perro = Mamifero('Carnivoro')

perro.reproducirse(6)
perro.crecer(43)

# imprimir datos
print("El tipo de alimentación del perro es", perro.alimentacion, 
      "mide", perro.altura, "cm", 
      "pesa", perro.peso, "kg", 
      "tuvo", perro.progenie, "crías")

# Cambiar atributos manualmente
perro.alimentacion = 'Omnívoro'
perro.altura = 43
perro.peso = 6.1
perro.progenie = 0

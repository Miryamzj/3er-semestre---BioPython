#si también necesitáramos una clase "mootrema" (mamíferos que ponen huevos), podemos

class monotrema(mamifero): 
    espolon= True

    def poner_huevos(self, max_huevos):
        huevos = 0

        for n in range(max_huevos):
            if choice([True, False]):
                huevos += 1 
        if huevos > 0: 
            self.reproducirse(huevos)

echidna= monotrema("carnivoro", 50, 6)
print ("El tipo de alimentacion de echidna es", echidna.alimentacion, ", mide" )                     

#Ejercicio4 

#Genera una función de longitud para la clase mRNA y para la clase proteína. La primera regresa el número de nucleótidos, y la segunda el número de nucleótidos y de aminoácidos



class ARNm: 
    def __init__(self, nombre_gen, secuencia_ARNm):
        self.nombre = nombre_gen
        self.secuencia_arnm = secuencia_ARNm.upper()          

    def obtener_longitud(self):
        return len(self.secuencia_arnm)
    
if secuencia_ARNm = True
    
    print(f"El ARNm tiene una longitud de {self.obtener_longitud()} ")




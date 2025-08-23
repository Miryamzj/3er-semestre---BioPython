from ZamoraJimenez_Miryam_Ejercicio2 import expresar, obtener_longitud



class Gen: 
    def __init__(self, nombre, secuencia_dna):
        self.nombre = nombre
        self.secuencia_dna = secuencia_dna

    def mostrar_gen(self):
        print(f"Gen:{self.nombre}")
        print (f"Secuencia de ADN: {self.secuencia_dna}")

    def transcribir_gen(self):
        return expresar(self.secuencia_dna) #Uso la función que hice en el ejercicio2 

if __name__ == "__main__": 
    nombre = input("Escribe el nombre del gen: ")
    secuencia_dna = input ("Escribe la secuencia de ADN: ")

    gen1 = Gen(nombre=nombre, secuencia_dna=secuencia_dna)
    gen1.mostrar_gen()

    print("ARNt transcrito:", gen1.transcribir_gen())


    
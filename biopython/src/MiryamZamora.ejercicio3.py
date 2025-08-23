from ZamoraJimenez_Miryam_Ejercicio2 import expresar, obtener_longitud

# Diccionario de codones a aminoacidos 
CODON_TABLA = {
    "AUG": "Met", "UUU": "Phe", "UUC": "Phe",
    "UUA": "Leu", "UUG": "Leu", "CUU": "Leu", "CUC": "Leu", "CUA": "Leu","CUG":"Leu",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", 
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val", 
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "UAU": "Tyr", "UAC": "Tyr",
    "CAU": "His", "CAC": "His", 
    "CAA": "Gln", "CAG": "Gln", 
    "AAU": "Asn", "AAC": "Asn",
    "AAA": "Lys", "AAG": "Lys",
    "GAU": "Asp", "GAC": "Asp", "GAA": "Asp", 
    "GAA": "Asp", "GAG": "Glu", 
    "UGU": "Cys", "UGC": "Cys", 
    "UGG": "Trp", 
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGC": "Arg", "AGA": "Arg", "AGG": "Arg", 
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
}

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


    
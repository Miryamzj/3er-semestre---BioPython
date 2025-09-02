CODON_TABLA = {
    "AUG": "Met", "UUU": "Phe", "UUC": "Phe",
    "UUA": "Leu", "UUG": "Leu", "CUU": "Leu", "CUC": "Leu",
    "CUA": "Leu", "CUG": "Leu", "AUU": "Ile", "AUC": "Ile",
    "AUA": "Ile", "GUU": "Val", "GUC": "Val", "GUA": "Val",
    "GUG": "Val", "UCU": "Ser", "UCC": "Ser", "UCA": "Ser",
    "UCG": "Ser", "CCU": "Pro", "CCC": "Pro", "CCA": "Pro",
    "CCG": "Pro", "ACU": "Thr", "ACC": "Thr", "ACA": "Thr",
    "ACG": "Thr", "UAU": "Tyr", "UAC": "Tyr", "CAU": "His",
    "CAC": "His", "CAA": "Gln", "CAG": "Gln", "AAU": "Asn",
    "AAC": "Asn", "AAA": "Lys", "AAG": "Lys", "GAU": "Asp",
    "GAC": "Asp", "GAA": "Glu", "GAG": "Glu", "UGU": "Cys",
    "UGC": "Cys", "UGG": "Trp", "CGU": "Arg", "CGC": "Arg",
    "CGA": "Arg", "AGA": "Arg", "AGG": "Arg", "GGU": "Gly",
    "GGC": "Gly", "GGA": "Gly", "GGG": "Gly", "UAA": "STOP",
    "UAG": "STOP", "UGA": "STOP"
}

class Gen:
    def __init__(self, nombre, secuencia_dna):
        self.nombre = nombre
        self.secuencia_dna = secuencia_dna.upper()

    def mostrar_gen(self):
        print(f"Gen: {self.nombre}")
        print(f"Secuencia de ADN: {self.secuencia_dna}")


class tRNA(Gen):
    def transcribir_gen(self):
        transcripcion = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
        arn = "".join(transcripcion.get(base, '') for base in self.secuencia_dna)
        return arn

    def longitud(self):
        return len(self.transcribir_gen())


class RNANoCodificante(Gen):
    def descripcion(self):
        return "Este ARN no codifica proteínas."


class Proteina(tRNA):
    def traducir(self):
        arn = self.transcribir_gen()
        aminoacidos = []
        for i in range(0, len(arn), 3):
            codon = arn[i:i+3]
            if len(codon) == 3:
                aa = CODON_TABLA.get(codon, '')
                if aa == "STOP":
                    break
                aminoacidos.append(aa)
        return aminoacidos

    def longitud(self):
        return {
            "nucleotidos": len(self.transcribir_gen()),
            "aminoacidos": len(self.traducir())
        }


if __name__ == "__main__":
    nombre = input("Escribe el nombre del gen: ")
    secuencia_dna = input("Escribe la secuencia de ADN: ")

    proteina = Proteina(nombre, secuencia_dna)
    proteina.mostrar_gen()
    print("ARNt transcrito:", proteina.transcribir_gen())
    print("Proteina traducida:", proteina.traducir())
    print("Longitudes:", proteina.longitud())

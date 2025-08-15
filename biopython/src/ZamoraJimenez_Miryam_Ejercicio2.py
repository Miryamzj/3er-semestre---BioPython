


secuencia_usuario = input(f"ingrese una secuencia de DNA:")

class Gen:
    def __init__(self, nombre, secuencia_dna, activo=True):
        self.nombre = nombre
        self.secuencia_dna = secuencia_dna.upper()
        self.activo = activo
        self.mensaje = None

    def expresar(self):
        if self.activo:
            # Diccionario para la transcripción de ADN a ARN
            transcripción = {
                 'A': 'U',
                 'T': 'A',
                 'G': 'C',
                 'C': 'G'
            }
            arn = "" 
            for base in self.secuencia_dna:
                arn+= transcripción.get(base, '?') #Si encuentra una letra desconocida, usa "?"
            self.mensaje = arn
            print(f"El gen {self.nombre} está siendo expresado.")
            print(f"ARN mensajero: {self.mensaje}")
        else:
            print(f"El gen {self.nombre} está inactivo. No se expresa.")
gen_usuario = Gen("GenUsuario",secuencia_usuario)
gen_usuario.expresar()            

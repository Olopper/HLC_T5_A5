class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    
    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.profesion}")

class Trabajador(Persona):
    def __init__(self, nombre, edad, profesion, sitio):
        super().__init__(nombre, edad, profesion)
        self.sitio = sitio
    
    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.profesion} y trabajo en {self.sitio}")

Elena = Trabajador("Elena", 35, "Arquitecta", "Construcciones XYZ")

Elena.presentarse()
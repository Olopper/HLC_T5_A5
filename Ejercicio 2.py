class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    
    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.profesion}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, profesion, asignatura):
        super().__init__(nombre, edad, profesion)
        self.asignatura = asignatura
    
    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.profesion} y estudio {self.asignatura}")

Carlos = Estudiante("Carlos", 22, "Estudiante", "Matemáticas")

Carlos.presentarse()

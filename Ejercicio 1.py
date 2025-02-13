class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    
    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre}, tengo {self.edad} y soy {self.profesion}")
    
Ana = Persona("Ana", 28, "Ingeniera")

Ana.presentarse()


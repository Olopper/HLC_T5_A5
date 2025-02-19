import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return math.pi * self.radio ** 2

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


              

c = Circulo(5)
r = Rectangulo(4, 6)
print(c.calcular_area())
print(r.calcular_area())
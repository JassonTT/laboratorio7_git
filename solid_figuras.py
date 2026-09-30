from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self) -> float:
        pass

class Rectangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

class Triangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

class Circulo(FiguraGeometrica):
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * (self.radio ** 2)

class CalculadoraArea:
    @staticmethod
    def imprimir_area(figura: FiguraGeometrica):
        print(f"El area de la figura es: {figura.calcular_area():.2f}")

if __name__ == "__main__":
    figuras = [
        Rectangulo(5, 10),
        Triangulo(4, 6),
        Circulo(3)
    ]
    for f in figuras:
        CalculadoraArea.imprimir_area(f)

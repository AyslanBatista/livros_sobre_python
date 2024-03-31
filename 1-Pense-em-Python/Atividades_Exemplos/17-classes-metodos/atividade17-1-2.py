"""
Como exercício, escreva um método init da classe Point que receba x e y
como parâmetros opcionais e os relacione aos atributos correspondentes.
"""


class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"valor de x: {self.x:.2f}\nvalor de y: {self.y:.2f}"


point = Point(4, 3)
print(point)

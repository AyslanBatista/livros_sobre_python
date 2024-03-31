"""
Como exercício, escreva um método add para Points que funcione com um
objeto Point ou com uma tupla:

Se o segundo operando for um Point, o método deve retornar um novo Point
cuja coordenada x é a soma das coordenadas x dos operandos, e o mesmo se
aplica às coordenadas de y.

Se o segundo operando for uma tupla, o método deve adicionar o primeiro
elemento da tupla à coordenada de x e o segundo elemento à coordenada de y,
retornando um novo Point com o resultado.
"""


class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"valor de x: {self.x:.2f}\nvalor de y: {self.y:.2f}"

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_other(other)
        else:
            return self.incremente(other)

    def add_other(self, other):
        sum_x = self.x + other.x
        sum_y = self.y + other.y
        return Point(sum_x, sum_y)

    def incremente(self, values):
        self.x += values[0]
        self.y += values[1]
        return Point(self.x, self.y)


point = Point(4, 3)
other_point = Point(5, 2)
print(point + other_point)
print(point + (3, 4))
# print(point)

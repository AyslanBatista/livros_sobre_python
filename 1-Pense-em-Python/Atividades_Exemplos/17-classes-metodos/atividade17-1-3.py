"""
Como exercício, escreva um método add para a classe Point.
"""


class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"valor de x: {self.x:.2f}\nvalor de y: {self.y:.2f}"

    def __add__(self, other):
        sum_x = self.x + other.x
        sum_y = self.y + other.y
        return Point(sum_x, sum_y)


point = Point(4, 3)
other_point = Point(5, 2)
print(point + other_point)
print(point)

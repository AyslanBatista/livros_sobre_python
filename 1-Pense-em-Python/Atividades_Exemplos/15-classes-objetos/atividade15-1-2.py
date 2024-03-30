"""
Como exercício, escreva uma função chamada move_rectangle que toma
um Rectangle e dois números chamados dx e dy. Ela deve alterar a posição
do retângulo, adicionando dx à coordenada x de corner e adicionando dy
à coordenada y de corner.
"""


class Rectangle:
    """Represents a rectangle.
    attributes: width, height, corner.
    """


box = Rectangle()

box.width = 50
box.height = 100


def move_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight


move_rectangle(box, 50, 100)

print(box.width)
print(box.height)

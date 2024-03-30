"""
Como exercício, escreva uma versão de move_rectangle que cria e retorne
um novo retângulo em vez de alterar o antigo.
"""

import copy


class Rectangle:
    """Represents a rectangle.
    attributes: width, height, corner.
    """


box = Rectangle()

box.width = 50
box.height = 100


def move_rectangle(rect, dwidth, dheight):
    new_rect = copy.deepcopy(rect)
    new_rect.width += dwidth
    new_rect.height += dheight
    return new_rect


new = move_rectangle(box, 50, 100)

print(new is box)

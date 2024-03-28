"""
Escreva uma função chamada middle que receba uma lista e retorne uma nova
lista com todos os elementos originais, exceto os primeiros e os últimos
elementos. Por exemplo:

>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]
"""

t = [1, 2, 3, 4]


def middle(t):
    return t[1:-1]


print(middle(t))

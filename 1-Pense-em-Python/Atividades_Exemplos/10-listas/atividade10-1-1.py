"""
Escreva uma função chamada nested_sum que receba uma lista de listas
de números inteiros e adicione os elementos de todas
as listas aninhadas. Por exemplo:

>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
"""

t = [[1, 2], [3], [4, 5, 6]]


def nested_sum(t):
    total = 0
    total = sum(sum(i) for i in t)
    return total


print(nested_sum(t))

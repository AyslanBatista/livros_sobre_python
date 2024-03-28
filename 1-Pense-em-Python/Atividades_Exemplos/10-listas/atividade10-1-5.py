"""
Escreva uma função chamada is_sorted que tome uma lista como parâmetro
e retorne True se a lista estiver classificada em ordem ascendente,
e False se não for o caso. Por exemplo:

>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False
"""

t = [1, 2, 3, 4]
t2 = [4, 2, 3, 1]


def is_sorted(lista):
    organizada = sorted(lista)
    if lista == organizada:
        return True
    else:
        return False


print(is_sorted(t2))

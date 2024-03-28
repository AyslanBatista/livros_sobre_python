"""
Escreva uma função chamada cumsum que receba uma lista de números
e retorne a soma cumulativa; isto é, uma nova lista onde o i-ésimo elemento
é a soma dos primeiros i+1 elementos da lista original. Por exemplo:

>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
"""

t = [1, 2, 3, 5, 6, 7]


def cumsum(t):
    total = sum(t)
    t.pop(len(t) - 1)
    t.append(total)
    return t


print(cumsum(t))

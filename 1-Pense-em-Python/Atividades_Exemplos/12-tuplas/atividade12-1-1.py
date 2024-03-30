"""
Como exercício, escreva uma função chamada sumall que receba qualquer número
de argumentos e retorne a soma deles.
"""


def sumall(*args):
    valores = list(args)
    return sum(valores)


print(sumall(1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 3, 4, 5, 6))

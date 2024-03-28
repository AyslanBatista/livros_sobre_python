"""
Um número a é uma potência de b se for divisível por b e a/b for
uma potência de b. Escreva uma função chamada is_power que receba
os parâmetros a e b e retorne True se a for uma potência de b.
Dica: pense no caso-base.
"""


def is_power(a, b):
    if a % b != 0:
        return False
    return is_power(a // b, b)


a = 8
b = 2

if is_power(a, b):
    print(f"{a} é uma potência de {b}")
else:
    print(f"{a} não é uma potência de {b}")

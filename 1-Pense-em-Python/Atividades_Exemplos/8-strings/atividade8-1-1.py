"""
Como exercício, escreva uma função que receba uma string como argumento
e exiba as letras de trás para a frente, uma por linha.
"""


def revertendo(word):
    letra = len(word) - 1
    while letra > -1:
        print(word[letra])
        letra -= 1


print(revertendo("testando"))

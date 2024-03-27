"""
Escreva uma função que desenhe uma grade semelhante com quatro linhas
e quatro colunas.
"""


def desenhar_grade():

    print(" " * 10, "+", "-", "-", "-", "+")
    for i in range(2):
        print(" " * 10, "|", " ", " ", " ", "|")
    print(" " * 10, "+", "-", "-", "-", "+")


desenhar_grade()

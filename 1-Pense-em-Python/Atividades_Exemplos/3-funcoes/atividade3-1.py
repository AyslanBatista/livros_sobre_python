"""
Escreva uma função chamada right_justify, que receba uma string chamada s
como parâmetro e exiba a string com espaços suficientes à frente para que
a última letra da string esteja na coluna 70 da tela:

Dica: Use concatenação de strings e repetição. Além disso, o Python
oferece uma função integrada chamada len, que apresenta o comprimento
de uma string, então o valor de len('monty') é 5.
"""


def right_justify(s):
    value = len(s)
    restante = 69 - value
    print(" " * restante, s)


name = "monty"
right_justify(name)

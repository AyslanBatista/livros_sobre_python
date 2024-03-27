"""
Escreva uma função que desenhe uma grade como a seguinte:
        + - - - - + - - - - +
        |         |         |
        |         |         |
        |         |         |
        |         |         |
        + - - - - + - - - - +
        |         |         |
        |         |         |
        |         |         |
        |         |         |
        + - - - - + - - - - +
        
Dica: para exibir mais de um valor em uma linha, podemos usar uma sequência
de valores separados por vírgula:

print('+', '-')
Por padrão, print avança para a linha seguinte, mas podemos ignorar esse
comportamento e inserir um espaço no fim, desta forma:

print('+', end=' ')
 print('-')
A saída dessas instruções é + -. Uma instrução print sem argumento termina
a linha atual e vai para a próxima linha.

"""


def desenhar_grade():
    for i in range(2):
        print(" " * 10, "+", "-", "-", "-", "-", "+", "-", "-", "-", "-", "+")
        for i in range(4):
            print(
                " " * 10, "|", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|"
            )
    print(" " * 10, "+", "-", "-", "-", "-", "+", "-", "-", "-", "-", "+")


desenhar_grade()

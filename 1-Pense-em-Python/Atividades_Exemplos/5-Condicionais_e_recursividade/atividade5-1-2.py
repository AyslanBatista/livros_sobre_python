"""
O último teorema de Fermat diz que não existem números inteiros a, b e c
tais que a**n + b**n == c**n para quaisquer valores de n maiores que 2.
"""


def check_fermat(a, b, c, n):
    valor1 = a**n + b**n
    valor2 = c**n
    if n > 2 and valor1 == valor2:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

"""
Defina uma função nova chamada do_four que receba um objeto de função
e um valor e chame a função quatro vezes, passando o valor como um parâmetro.
Deve haver só duas afirmações no corpo desta função, não quatro.
"""


def do_four(f, valor):
    for i in range(4):
        f(valor)


def print_valor(valor):
    print(valor)


do_four(print_valor, "Olá, mundo!")

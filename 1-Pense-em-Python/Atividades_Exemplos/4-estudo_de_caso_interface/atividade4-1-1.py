"""
Escreva uma função chamada square que receba um parâmetro chamado t,
que é um turtle. Ela deve usar o turtle para desenhar um quadrado.
Escreva uma chamada de função que passe bob como um argumento para
o square e então execute o programa novamente.
"""

import turtle

bob = turtle.Turtle()


def square(t):
    for i in range(4):
        t.forward(100)
        t.right(90)


square(bob)


turtle.done()

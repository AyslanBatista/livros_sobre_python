"""
Escreva uma função chamada circle que use o turtle, t e um raio r como
parâmetros e desenhe um círculo aproximado ao chamar polygon com um
comprimento e número de lados adequados.
Teste a sua função com uma série de valores de r.


Dica: descubra a circunferência do círculo e certifique-se
de que length * n = circumference.
"""

import math
import turtle


def polygon(t, n, side_length):

    for i in range(n):
        t.forward(side_length)
        t.right(360 / n)


def circle(t, r, n=360):

    circumference = 2 * math.pi * r
    side_length = circumference / n
    polygon(t, n, side_length)


bob = turtle.Turtle()

for radius in range(10, 100, 10):
    circle(bob, radius)

turtle.done()

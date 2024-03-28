"""
Faça uma cópia do square e mude o nome para polygon. Acrescente outro
parâmetro chamado n e altere o corpo para que desenhe um polígono
regular de n lados.

Dica: os ângulos exteriores de um polígono regular de n lados são 360/n graus.
"""

import turtle


def polygon(t, n, side_length):

    for i in range(n):
        t.forward(side_length)
        t.right(360 / n)


bob = turtle.Turtle()

polygon(bob, 5, 100)


turtle.done()

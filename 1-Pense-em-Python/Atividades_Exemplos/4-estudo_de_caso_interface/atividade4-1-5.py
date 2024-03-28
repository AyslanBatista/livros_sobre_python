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


def arc(t, r, n, angle):
    circumference = 2 * math.pi * r
    side_length = circumference / n
    turn_angle = angle / n
    for i in range(int(angle / turn_angle)):
        t.forward(side_length)
        t.right(turn_angle)


# Exemplo de uso
bob = turtle.Turtle()

arc(bob, 50, 360, 90)
arc(bob, 50, 360, 180)
arc(bob, 50, 360, 360)

turtle.done()

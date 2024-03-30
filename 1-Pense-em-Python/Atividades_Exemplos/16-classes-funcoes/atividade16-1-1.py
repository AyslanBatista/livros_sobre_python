"""
Como exercício, escreva uma função chamada print_time, que receba
um objeto Time e o exiba na forma hour:minute:second. Dica: a sequência
de formatação '%.2d' exibe um número inteiro com, pelo menos, dois dígitos,
incluindo um zero à esquerda, se for necessário.

Escreva uma função booleana chamada is_after, que receba dois objetos Time,
t1 e t2, e devolva True se t1 for cronologicamente depois de t2 e False se
não for. Desafio: não use uma instrução if.
"""

import copy


class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """


time = Time()
time.hour = 11
time.minute = 47
time.second = 30

timet2 = copy.deepcopy(time)
time.hour = 10
time.minute = 27
time.second = 50


def print_time(object):
    # return "%.2d:%.2d:%.2d" % (object.hour, object.minute, object.second)
    return f"{object.hour}:{object.minute}:{object.second}"


def is_after(t1, t2):
    t1_seconds = t1.hour * 3600 + t1.minute * 60 + t1.second
    t2_seconds = t2.hour * 3600 + t2.minute * 60 + t2.second
    return t1_seconds > t2_seconds


print(is_after(time, timet2))

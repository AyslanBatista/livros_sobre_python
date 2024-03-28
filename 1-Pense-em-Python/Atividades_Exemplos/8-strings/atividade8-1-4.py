"""As seguintes funções pretendem verificar se uma string contém alguma
letra minúscula, mas algumas delas estão erradas. Para cada função,
descreva o que ela faz (assumindo que o parâmetro seja uma string).
"""


def any_lowercase1(s):
    """Errada"""
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """Errada"""
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """Errada"""
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Correta"""
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """Errada"""
    for c in s:
        if not c.islower():
            return False
    return True


testando = "testaNDO"
print(any_lowercase5(testando))

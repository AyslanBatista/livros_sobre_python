"""
Digite essas funções em um arquivo chamado palindrome.py e teste-as.
O que acontece se chamar middle com uma string de duas letras? Uma letra?
E se a string estiver vazia, escrita com '' e não contiver nenhuma letra?
"""


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


print(middle("ss"))

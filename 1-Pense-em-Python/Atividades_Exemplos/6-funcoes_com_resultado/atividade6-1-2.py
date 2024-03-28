"""
Digite essas funções em um arquivo chamado palindrome.py e teste-as.
O que acontece se chamar middle com uma string de duas letras? Uma letra?
E se a string estiver vazia, escrita com '' e não contiver nenhuma letra?
"""


def is_palindrome(word):
    new_word = "".join(reversed(word))
    if word == new_word:
        return True
    else:
        return False


print(is_palindrome("reviver"))

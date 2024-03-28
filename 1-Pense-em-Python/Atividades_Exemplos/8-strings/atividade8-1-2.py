"""
Como exercício, encapsule este código em uma função denominada count
e generalize-o para que aceite a string e a letra como argumentos.
"""


def count(word, letra):
    quantidade = 0
    for letter in word:
        if letter == letra:
            quantidade += 1
    return quantidade


print(count("banana", "a"))

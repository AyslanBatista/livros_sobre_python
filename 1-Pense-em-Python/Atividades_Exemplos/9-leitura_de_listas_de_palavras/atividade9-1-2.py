"""
Escreva uma função chamada has_no_e que retorne True se a palavra
dada não tiver a letra “e” nela.

Altere seu programa na seção anterior para imprimir apenas as palavras
que não têm “e” e calcule a porcentagem de palavras na lista que não têm “e”.
"""

import os

path = os.curdir
WORDS_FILE = "words.txt"
filepath = os.path.join(path, WORDS_FILE)


def has_no_e(word):
    if "e" in word:
        return True
    else:
        return False


def checkando_lista(lista):
    numero = 0
    for line in open(lista):
        word = line.strip()
        if has_no_e(word):
            numero += 1
    return numero


def calculando_porcentagem(valores):
    with open(valores, "r") as file_:
        linhas = file_.readlines()
        total = len(linhas)
    parcial = checkando_lista(valores)
    return (parcial / total) * 100


print(calculando_porcentagem(filepath))

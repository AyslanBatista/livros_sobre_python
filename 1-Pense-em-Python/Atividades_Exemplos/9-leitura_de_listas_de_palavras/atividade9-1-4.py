"""
Escreva uma função chamada is_abecedarian que retorne True se as letras
numa palavra aparecerem em ordem alfabética (tudo bem se houver letras duplas).
Quantas palavras em ordem alfabética existem?
"""

import os

path = os.curdir
WORDS_FILE = "words.txt"
filepath = os.path.join(path, WORDS_FILE)


def ordem_alfabetica(word):
    alfabetico = "".join(sorted(word))
    if word == alfabetico:
        return True
    else:
        return False


def checkando_lista(lista):
    numero = 0
    for line in open(lista):
        word = line.strip()
        if ordem_alfabetica(word):
            numero += 1
    return numero


def calculando_porcentagem(valores):
    with open(valores, "r") as file_:
        linhas = file_.readlines()
        total = len(linhas)
    parcial = checkando_lista(valores)
    return (parcial / total) * 100


print(calculando_porcentagem(filepath))

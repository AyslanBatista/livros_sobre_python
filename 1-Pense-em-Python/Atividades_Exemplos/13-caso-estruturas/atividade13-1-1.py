"""
Escreva um programa que leia um arquivo, quebre cada linha em palavras,
remova os espaços em branco e a pontuação das palavras, e as converta
em letras minúsculas.

Dica: O módulo string oferece uma string chamada whitespace, que contém espaço,
tab, newline etc., e punctuation, que contém os caracteres de pontuação.
Vamos ver se conseguimos fazer o Python falar palavrões:
>>> import string
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
"""

import cProfile
import os
import string

path = os.curdir
WORDS_FILE = "words.txt"
filepath = os.path.join(path, WORDS_FILE)


def diferenca_listas(filepath):
    lista_antiga = [linha.strip() for linha in open(filepath).readlines()]
    lista_nova = []
    with open(filepath, "r") as file_:
        for linha in file_:
            palavra = linha.lower()
            nova_palavra = palavra.translate(
                str.maketrans("", "", string.whitespace + string.punctuation)
            )
            lista_nova.append(nova_palavra)

    diferenca = set(lista_antiga) - set(lista_nova)

    return print(diferenca)


profiler = cProfile.Profile()

profiler.runcall(diferenca_listas, filepath)

profiler.print_stats()

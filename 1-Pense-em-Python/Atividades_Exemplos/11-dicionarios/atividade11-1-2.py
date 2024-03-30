"""
Escreva uma função que leia as palavras em words.txt e guarde-as como
chaves em um dicionário. Não importa quais são os valores.
Então você pode usar o operador in como uma forma rápida de verificar
se uma string está no dicionário.

"""

import cProfile
import os

path = os.curdir
WORDS_FILE = "words.txt"
filepath = os.path.join(path, WORDS_FILE)


def hash_dict(list):
    palavras = dict()
    for line in open(list):
        word = line.strip()
        palavras[word] = None
    if "sentinelling" in palavras:
        return True
    else:
        return False


hash_dict(filepath)

# Cria um objeto cProfile
profiler = cProfile.Profile()

# Executa a função hash_dict com profiling
profiler.runcall(hash_dict, filepath)

# Imprime o relatório de desempenho
profiler.print_stats()

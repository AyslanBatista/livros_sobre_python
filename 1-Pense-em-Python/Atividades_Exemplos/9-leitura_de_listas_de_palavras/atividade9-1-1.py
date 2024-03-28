"""
Escreva um programa que leia words.txt e imprima apenas as palavras
com mais de 20 caracteres (sem contar whitespace)
"""

import os

path = os.curdir
WORDS_FILE = "words.txt"
filepath = os.path.join(path, WORDS_FILE)

for line in open(filepath):
    word = line.strip()
    if len(word) >= 20:
        print(word)

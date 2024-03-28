"""
Escreva uma função chamada avoids que receba uma palavra e uma série
de letras proibidas, e retorne True se a palavra não usar nenhuma
das letras proibidas.

Altere o código para que o usuário digite uma série de letras proibidas
e o programa imprima o número de palavras que não contêm nenhuma delas.
Você pode encontrar uma combinação de cinco letras proibidas que exclua
o menor número possível de palavras?
"""

import os

path = os.curdir
WORDS_FILE = "words.txt"
filepath = os.path.join(path, WORDS_FILE)


while True:
    letras_proibidas = []
    letra = input("Informe uma letra proibida: ")
    letras_proibidas.append(letra)
    if input(
        "Deseja escrever mais alguma letra? se sim aperte enter,"
        "se não aperta qualquer outra tecla."
    ):
        break


def verificando_palavras(word, lista_letras):
    for letra in lista_letras:
        if letra in word:
            return True
        else:
            return False


def checkando_lista(lista, letras):
    numero = 0
    for line in open(lista):
        word = line.strip()
        if verificando_palavras(word, letras):
            numero += 1
    return numero


def calculando_porcentagem(valores):
    with open(valores, "r") as file_:
        linhas = file_.readlines()
        total = len(linhas)
    parcial = checkando_lista(valores, letras_proibidas)
    return (parcial / total) * 100


print(calculando_porcentagem(filepath))

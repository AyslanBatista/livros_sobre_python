"""
Uma cifra de César é uma forma fraca de criptografia que implica “rotacionar”
cada letra por um número fixo de lugares. Rotacionar uma letra significa
deslocá-lo pelo alfabeto, voltando ao início se for necessário, portanto
'A' rotacionado por 3 é 'D' e 'Z' rotacionado por 1 é 'A'.

Para rotacionar uma palavra, faça cada letra se mover pela mesma quantidade
de posições. Por exemplo, “cheer” rotacionado por 7 é “jolly” e “melon”
rotacionado por -10 é “cubed”. No filme 2001: Uma odisseia no espaço,
o computador da nave chama-se HAL, que é IBM rotacionado por -1.

Escreva uma função chamada rotate_word que receba uma string e um número
inteiro como parâmetros, e retorne uma nova string que contém as letras
da string original rotacionadas pelo número dado.
"""


def rotate_word(word, numero):
    palavra = word.lower()
    nova_palavra = []
    for letter in palavra:
        valor = ord(letter)
        nova_letra = valor + numero
        if nova_letra > 122:
            nova_letra = 96 + (-(122 - nova_letra))
            nova_palavra.append(nova_letra)
        else:
            nova_palavra.append(nova_letra)

    palavra_rotacionada = []
    for letter_rotacionada in nova_palavra:
        palavra_rotacionada.append(chr(letter_rotacionada))

    return "".join(palavra_rotacionada)


print(rotate_word("ayslan", 2))

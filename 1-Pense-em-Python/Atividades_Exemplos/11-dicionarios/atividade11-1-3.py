import cProfile
import os

path = os.curdir
WORDS_FILE = "words.txt"
filepath = os.path.join(path, WORDS_FILE)


def in_bisect(lista_ordenada, valor_alvo):
    with open(lista_ordenada, "r") as file_:
        linhas = file_.readlines()
        lista = [linha.strip() for linha in linhas]
        baixo = 0
        alto = len(linhas) - 1

        while baixo <= alto:
            meio = (baixo + alto) // 2

            if lista[meio] == valor_alvo:
                return meio

            elif lista[meio] < valor_alvo:
                baixo = meio + 1

            else:
                alto = meio - 1

    return None


# Exemplo de uso
lista_palavras = filepath
palavra_alvo = "sentinelling"

indice = in_bisect(lista_palavras, palavra_alvo)

if indice is not None:
    print(f"A palavra '{palavra_alvo}' está na lista no índice {indice}.")
else:
    print(f"A palavra '{palavra_alvo}' não está na lista.")


# Cria um objeto cProfile
profiler = cProfile.Profile()

# Executa a função hash_dict com profiling
profiler.runcall(in_bisect, lista_palavras, palavra_alvo)

# Imprime o relatório de desempenho
profiler.print_stats()

"""
Escreva uma função chamada eval_loop que iterativamente peça uma entrada
ao usuário, a avalie usando eval e exiba o resultado.

Ela deve continuar até que o usuário digite done; então deverá exibir
o valor da última expressão avaliada.
"""


def eval_loop():
    resultado = None
    while True:
        expressao = input("Digite uma expressão (ou 'done' para sair): ")
        if expressao == "done":
            break
        try:
            resultado = eval(expressao)
        except Exception as e:
            print(f"Erro: {e}")
        else:
            print(f"Resultado: {resultado}")

    if resultado is not None:
        print(f"Valor final: {resultado}")


eval_loop()

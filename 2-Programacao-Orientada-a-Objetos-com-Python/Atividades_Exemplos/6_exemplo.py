# Parâmetros que se tornarão variáveis(objetos) internos da função
class Pessoa:
    def __init__(self, nome, idade, sexo, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura


pessoa1 = Pessoa("Fernando", 21, "M", 1.90)

print(pessoa1.nome, pessoa1.idade)

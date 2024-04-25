class Pessoa:
    def __init__(self, nome, idade, sexo=False, altura=False):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura


pessoa1 = Pessoa("Fernando", 32, "M", 1.90)
pessoa2 = Pessoa("Maria", 31)


print(pessoa1.nome, pessoa1.altura)
print(pessoa2.nome, pessoa1.idade)

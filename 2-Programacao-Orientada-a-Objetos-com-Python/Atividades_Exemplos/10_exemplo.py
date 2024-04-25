class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        ano_nas = self.ano_atual - self.idade
        print(f"Seu ano de nascimento é {ano_nas}")


pessoa1 = Pessoa("Fernando", 32)

print(pessoa1.ano_nascimento())

class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # classe dinâmica, retorno é de escopo global
    @classmethod
    def ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


pessoa2 = Pessoa.ano_nascimento("Fernando", 1987)

print(pessoa2.idade)

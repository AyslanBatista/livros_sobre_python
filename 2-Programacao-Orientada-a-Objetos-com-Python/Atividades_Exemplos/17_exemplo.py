class Contato:
    def __init__(self, residencial, celular):
        self.residencial = residencial
        self.celular = celular


class Cliente:
    def __init__(self, nome, idade, fone=None):
        self.nome = nome
        self.idade = idade
        self.fone = []

    def add_fone(self, residencial, celular):
        self.fone.append(Contato(residencial, celular))

    def lista_fone(self):
        for fone in self.fone:
            print(fone.residencial, fone.celular)


cliente1 = Cliente("Fernando", 32)
cliente1.add_fone(33213231, 432412321)

print(cliente1.nome)
print(cliente1.lista_fone)

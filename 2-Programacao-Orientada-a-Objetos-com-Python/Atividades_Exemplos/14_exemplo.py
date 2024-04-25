class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def preco(self):
        return self.preco_valido

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace("R$", ""))

        self.preco_valido = valor


produto1 = Produto("Processador", 370)
produto1.desconto(15)


produto2 = Produto("Placa Mãe", "R$280")
produto2.desconto(20)


print(produto1.preco)
print(produto2.preco)

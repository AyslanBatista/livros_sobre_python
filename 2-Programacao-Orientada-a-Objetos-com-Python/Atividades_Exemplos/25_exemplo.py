class Caixa:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def __add__(self, other):
        largura1 = self.largura + other.largura
        altura1 = self.altura + other.altura
        return Caixa(largura1, altura1)

    def __repr__(self):
        return f"<class 'Caixa({self.largura}, {self.altura})'>"


caixa1 = Caixa(10, 10)
caixa2 = Caixa(10, 20)

caixa3 = caixa1 + caixa2

print(caixa3)

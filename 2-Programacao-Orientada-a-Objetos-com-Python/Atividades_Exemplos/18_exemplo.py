# MODO ERRADO, REPETITIVO
class Corsa:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano


class Gol:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano



# MODO CORRETO DE FAZER
class Carro:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano


class Corsa(Carro):
    pass


class Gol(Carro):
    pass

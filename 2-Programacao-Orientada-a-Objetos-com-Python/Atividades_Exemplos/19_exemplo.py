class Carro:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano


class Gasolina(Carro):
    def __init__(self, tipogasolina=True, tipoalcool=False):
        self.tipogasolina = tipogasolina
        self.tipoalcool = tipoalcool


class Jeep(Gasolina):
    pass


# MODO NÂO USUAL
class Jeep:
    def carro():
        def __init__(self, nome, ano):
            self.nome = nome
            self.ano = ano

    def gasolina(self, tipogasolina=True, tipoalcool=False):
        self.tipogasolina = tipogasolina
        self.tipoalcool = tipoalcool

jeep = Jeep()

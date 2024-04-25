from random import randint


class Pessoa:
    @staticmethod
    def gerador_id():
        gerador = randint(100, 999)
        return gerador


print(Pessoa.gerador_id())

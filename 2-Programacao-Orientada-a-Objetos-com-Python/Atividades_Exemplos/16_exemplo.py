class Usuario:
    def __init__(self, nome):
        self.__nome = nome
        self.__logar = None

    @property
    def nome(self):
        return self.__nome

    @property
    def logar(self):
        return self.__logar

    @logar.setter
    def logar(self, logar):
        self.__logar = logar


class Identificador:
    def __init__(self, numero):
        self.__numero = numero

    @property
    def numero(self):
        return self.__numero

    def logar(self):
        print("logando no sistema...")


usuario1 = Usuario("Fernando")
identificador1 = Identificador("0001")

usuario1.logar = identificador1
usuario1.logar.logar()

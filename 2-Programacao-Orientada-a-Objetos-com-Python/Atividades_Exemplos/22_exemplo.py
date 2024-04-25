class Pessoa:
    def Acao(self):
        print("Inicializando o sistema")


class Acao1(Pessoa):
    def Acao(self):
        print("Sistema pronto para uso")


class Acao2(Pessoa):
    def acao(self):
        print("Desligando o sistema")


class SaveJogador1(Acao1, Acao2):
    pass


p1 = SaveJogador1()
p1.acao

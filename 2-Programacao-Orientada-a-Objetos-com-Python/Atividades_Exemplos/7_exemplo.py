class Pessoa:
    administrador = "Admin"

    def __init__(self, nome):
        self.nome = nome

        msg = "Classe Pessoa em execução"
        print(msg)

    def metodo1(self):
        print(msg)
        pass


var1 = Pessoa("Fernando")

print(var1)

# NameError, msg é uma variavel interna de __init__
# inacessível para outras funções da mesma classe.
# print(var1.metodo1())


# Forma correta de fazer:
class Pessoa:
    administrador = "Admin"

    def __init__(self, nome, msg):
        self.nome = nome
        self.msg = msg
        print(msg)

    def metodo1(self, msg):
        print(msg)
        pass


var1 = Pessoa("Fernando", "classe pessoa em execução")


print(var1.metodo1)

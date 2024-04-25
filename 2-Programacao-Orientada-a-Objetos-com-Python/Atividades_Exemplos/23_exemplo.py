from abc import ABC, abstractclassmethod


class Pessoa(ABC):
    @abstractclassmethod
    def logar(self):
        pass


class Usuario(Pessoa):
    def logar(self):
        print("Usuario logado no sistema")


# Não é possível inicializar a classe abstrata
# user1 = Pessoa()

user1 = Usuario()
user1.logar()

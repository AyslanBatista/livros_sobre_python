from abc import ABC, abstractclassmethod


class Pessoa(ABC):
    @abstractclassmethod
    def logar(self, chaveseguranca):
        pass


class Usuario(Pessoa):
    def logar(self, chaveseguranca):
        print("Usuario logado no sistema")


class Bot(Pessoa):
    def logar(self, chaveseguranca):
        print("Sistema rodando em segundo plano")


user1 = Usuario()

user1.logar("i5m8b4y9")

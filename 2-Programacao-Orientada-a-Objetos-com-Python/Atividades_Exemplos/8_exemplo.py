class Pessoa:
    pessoa1 = "Admin"
    # pessoa1 faz parte do escopo global da classe
    # pessoa1 é instanciável por qualquer método

    def __init__(self, pessoa2):
        self.pessoa2 = pessoa2
        # pessoa2 faz parte do escopo do método construtor
        # pessoa2 é acessível dentro e fora deste método
        # pessoa2 pode ser instanciada fora da classe

        pessoa3 = "DefaultUser"
        # pessoa3 faz parte do escopo do método construtor
        # pessoa3 é acessível somente dentro deste método

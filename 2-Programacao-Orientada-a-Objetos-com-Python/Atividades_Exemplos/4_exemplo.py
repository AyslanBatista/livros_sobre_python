# Variavel nome com um atributo próprio
class Pessoa:
    nome = "Padrão"


pessoa1 = Pessoa()

# Realizando alteração no atributo
pessoa1.nome = "Fernando"

print(pessoa1.nome)


# CUIDADO
pessoa1 = Pessoa()
pessoa2 = Pessoa()
pessoa3 = Pessoa()

# Isso ira alterar todas as instancias
Pessoa.nome = "Fernando"

print(pessoa1)
print(pessoa2)
print(pessoa3)

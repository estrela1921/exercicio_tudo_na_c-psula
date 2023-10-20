class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    # Métodos para acessar os atributos (getters)
    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    # Métodos para alterar os atributos (setters)
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

# Demonstração do funcionamento da classe Pessoa
pessoa1 = Pessoa("João da Silva", "123.456.789-00")
print("Nome:", pessoa1.get_nome())
print("CPF:", pessoa1.get_cpf())

# Alterando o nome e o CPF
pessoa1.set_nome("Maria Souza")
pessoa1.set_cpf("987.654.321-00")

print("\nDepois de alterar os atributos:")
print("Nome:", pessoa1.get_nome())
print("CPF:", pessoa1.get_cpf())

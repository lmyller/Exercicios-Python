from Validar_CPF.ValidarCPF import cpf


class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def idade(self):
        return self.__idade

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        if cpf(cpf):
            self.__cpf = cpf
            return True

        return False

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

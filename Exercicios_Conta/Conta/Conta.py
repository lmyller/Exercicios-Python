from abc import ABC


class Conta(ABC):
    def __init__(self, agencia, conta, valor):
        self.__agencia = agencia
        self.__conta = conta
        self.__valor = valor

    @property
    def agencia(self):
        return self.__agencia

    @property
    def conta(self):
        return self.__conta

    def saldo(self):
        return self.__valor

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia
    
    @conta.setter
    def conta(self, conta):
        self.__conta = conta

    def deposito(self, valor):
        if not isinstance(valor, (int, float)):
            return False

        self.__valor += valor
        return True

    def saque(self, valor):
        if not isinstance(valor, (int, float)):
            return False

        if valor > self.__valor:
            return False
        
        self.__valor -= valor

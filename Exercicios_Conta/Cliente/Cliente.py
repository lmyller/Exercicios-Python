from Pessoa import Pessoa
from Conta import ContaCorrente, ContaPoupanca


class Cliente(Pessoa):
    def __init__(self, nome, cpf, idade):
        super().__init__(nome, cpf, idade)
        self.__contas = []

    def adicionarConta(self, agencia, conta, saldo, limite=0):
        if limite == 0:
            self.__contas.append(ContaPoupanca(agencia, conta, saldo))

        else:
            self.__contas.append(ContaCorrente(agencia, conta, saldo, limite))

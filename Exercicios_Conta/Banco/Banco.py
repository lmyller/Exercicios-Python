from Cliente import Cliente
from Conta import ContaCorrente, ContaPoupanca


class Banco:
    def __init__(self):
        self.__clientes = []
        self.__contas = []

    def adicionarContaCorrente(self, agencia, conta, saldo, limite):
        self.__contas.append(ContaCorrente(agencia, conta, saldo, limite))

    def adicionarContaPoupanca(self, agencia, conta, saldo):
        self.__contas.append(ContaPoupanca(agencia, conta, saldo))

    def obterConta(self, posicao):
        return self.__contas[posicao]

    def quantidadeContas(self):
        return len(self.__contas)
    
    def adicionarCliente(self, nome, cpf, idade):
        self.__clientes.append(Cliente(self, nome, cpf, idade))

    def obterCliente(self, posicao):
        return self.__clientes[posicao]

    def quantidadeClientes(self):
        return len(self.__clientes)
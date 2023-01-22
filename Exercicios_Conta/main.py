from Banco import Banco

DIGITE_MOME = 'Nome: '
DIGITE_CPF = 'CPF: '
DIGITE_IDADE = 'Idade: '

banco = Banco()

def cadastrar_cliente():
    nome = input(DIGITE_MOME)
    print(nome)

while(True):
    opcao = int(input('1- Cadastrar cliente\n2- Cadastrar conta\n3- Saque\n4- Depósito'))
    match opcao:
        case 1: 
            cadastrar_cliente()

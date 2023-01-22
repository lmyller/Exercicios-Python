from RetiraCaracteres.RetiraCaracteres import retirarHifen, retirarPonto


def verificarNumerosIguais(cpf):
    cpfOrdenado = list(cpf)
    cpfOrdenado.sort()

    return True if cpfOrdenado[0] == cpfOrdenado[8] else False


def encontrarDigito(cpf, multiplicador):
    soma = 0

    for indice, multi in enumerate(range(multiplicador, 1, -1)):
        soma += cpf[indice] * multi

    digito = 11 - (soma % 11)
    return digito if digito <= 9 else 0


def validarCpf(cpf):
    cpf = list(map(int, cpf))

    if verificarNumerosIguais(cpf):
        return False

    digito1 = encontrarDigito(cpf, len(cpf) - 1)
    digito2 = encontrarDigito(cpf, len(cpf))

    return True if digito1 == cpf[len(cpf) - 2] and digito2 == cpf[len(cpf) - 1] else False


cpf = input('CPF: ')

if len(cpf) == 14:
    cpf = retirarPonto(cpf)
    cpf = retirarHifen(cpf)

    cpf = list(cpf)

    if len(cpf) == 11:
        if validarCpf(cpf):
            print('CPF válido')
else:
    print('CPF inválido')

from RetiraCaracteres import RetiraCaracteres


def verificar_numeros_iguais(cpf):
    cpfOrdenado = list(cpf)
    cpfOrdenado.sort()

    return True if cpfOrdenado[0] == cpfOrdenado[8] else False


def encontrar_digito(cpf, multiplicador):
    soma = 0

    for indice, multi in enumerate(range(multiplicador, 1, -1)):
        soma += cpf[indice] * multi

    digito = 11 - (soma % 11)
    return digito if digito <= 9 else 0


def validar_cpf(cpf):
    cpf = list(map(int, cpf))

    if verificar_numeros_iguais(cpf):
        return False

    digito1 = encontrar_digito(cpf, len(cpf) - 1)
    digito2 = encontrar_digito(cpf, len(cpf))

    return True if digito1 == cpf[len(cpf) - 2] and digito2 == cpf[len(cpf) - 1] else False


def receber_cpf(cpf):
    if len(cpf) == 14:
        cpf = RetiraCaracteres.retirarPonto(cpf)
        cpf = RetiraCaracteres.retirarHifen(cpf)

        cpf = list(cpf)

        if len(cpf) == 11:
            if validar_cpf(cpf):
                return True

        return False

    else:
        return False


cpf = input('CPF: ')

receber_cpf(cpf)

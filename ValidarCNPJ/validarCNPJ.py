from RetiraCaracteres.RetiraCaracteres import removerCaracteres


def validar_digito(cnpj, final):
    soma = 0

    if final == len(cnpj) - 2:
        multplicador = 5

    else:
        multplicador = 6

    for indice in range(final):
        soma += cnpj[indice] * multplicador
        multplicador -= 1
        if multplicador == 1:
            multplicador = 9

    digito = 11 - (soma % 11)
    return digito if digito <= 9 else 0


def validar_cnpj(cnpj):
    cnpj = removerCaracteres(cnpj)
    cnpj = list(cnpj)
    cnpj = list(map(int, cnpj))

    digito1 = validar_digito(cnpj, len(cnpj) - 2)
    digito2 = validar_digito(cnpj, len(cnpj) - 1)

    if digito1 == cnpj[len(cnpj) - 2] and digito2 == cnpj[len(cnpj) - 1]:
        print('CNPJ válido!')

    else:
        print('CNPJ inválido!')


cnpj = input('CNPJ: ')

if len(cnpj) == 18:
    validar_cnpj(cnpj)

else:
    print('CNPJ inválido')

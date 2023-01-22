def retirar_ponto(string):
    string = string.replace('.', '')
    return string


def retirar_hifen(string):
    string = string.replace('-', '')
    return string


def retirar_barra(string):
    string = string.replace('/', '')
    return string


def removerCaracteres(string):
    string = retirar_ponto(string)
    string = retirar_hifen(string)
    string = retirar_barra(string)

    return string

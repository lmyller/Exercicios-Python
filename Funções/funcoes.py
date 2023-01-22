def saudacao(saudacao, nome):
    print(saudacao, nome)

def soma(num1, num2, num3):
    print(num1 + num2 + num3)

def aumento(numero, porcentagem):
    return numero + (numero * porcentagem / 100)

def fizzBuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'FizzBuzz'

    if numero % 3 == 0:
        return 'Fizz'
    
    if numero % 5 == 0:
        return 'Buzz'
    
    return numero

for numero in range(101):
    print(fizzBuzz(numero))

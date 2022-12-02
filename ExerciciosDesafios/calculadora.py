import math
def somar(valorA, valorB):
    resultado = valorA + valorB
    print(f"Resultado da soma é: {resultado}")

def subtrair(valorA, valorB):
    resultado = valorA - valorB
    print(f"Resultado da subtração é: {resultado}")

def multiplicacao(valorA, valorB):
    resultado = valorA * valorB
    print(f"Resultado da multiplicação é: {resultado}")

def divisao(valorA, valorB):
    resultado = valorA / valorB
    print(f"Resultado da divisão é: {resultado:.3f}")

def potencia(valorA, valorB):
    resultado = valorA ** valorB
    print(f"Resultado da potência é: {resultado:.3f}")

def raiz(valorA, valorB):
    raiz1 = math.sqrt(valorA)
    raiz2 = math.sqrt(valorB)
    print(f'''A raiz de {valorA} é {raiz1:.3f}
A raiz de {valorB} é {raiz2:.3f}''')

def porcentagem(valorA, valorB):
    resultado = ((valorB)/100)*valorA
    print(f"Resultado da porcentagem é: {resultado:.3f}")

while True:
    opcao = int (input('''
    1- somar
    2- subtração
    3- multiplicação
    4- divisão
    5- potência
    6- raiz
    7- porcentagem
    Sua opção é: '''))
    if opcao != 1 or opcao != 2 or opcao != 3 or opcao != 4 or opcao != 5 or opcao != 6 or opcao != 7 :
        print('\n')
        print('Insira um valor válido')

        opcao = int(input('''
        1- somar
        2- subtração
        3- multiplicação
        4- divisão
        5- potência
        6- raiz
        7- porcentagem
        Sua opção é: '''))

    valor1 = int (input("digite um valor que deseja: "))
    valor2 = int (input("digite o outro valor que deseja: "))

    if opcao == 1:
        somar(valor1, valor2)
    elif opcao == 2:
        subtrair(valor1, valor2)
    elif opcao == 3:
        multiplicacao(valor1, valor2)
    elif opcao == 4:
        divisao(valor1, valor2)
    elif opcao == 5:
        potencia(valor1, valor2)
    elif opcao == 6:
        raiz(valor1, valor2)
    elif opcao == 7:
        porcentagem(valor1, valor2)


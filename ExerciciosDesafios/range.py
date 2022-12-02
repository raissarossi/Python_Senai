from datetime import datetime


# DESAFIO 1
# Crie um programa que peça ao usuário um número (N) e depois a quantidade de vezes que
# esse número deve ser multiplicado (Y). Exiba o resultado para cada uma das multiplicações
# realizadas
for x in range(0,6):
    print(f'O valor de 3 x {x} é: {3 * x }')


# DESAFIO 2
# Faça um programa que peça o ano de nascimento de 5 pessoas.
# Ao final, mostre quantas pessoas são maiores de idade (maior que 18)
num = 2
contador = 0
for age in range(num):
    dia= int(input('QUE DIA VOCÊ NASCEU? '))
    mes= int(input('QUE MÊS VOCÊ NASCEU? '))
    ano= int(input('QUE ANO VOCÊ NASCEU? '))
    ano_atual= int(datetime.now().year)
    mes_atual= int(datetime.now().month)
    dia_atual= int(datetime.now().day)
    anoo= ano_atual - ano
    if anoo > 18:
        contador += 1

    if anoo == 18:
        if mes_atual > mes:
            contador += 1
        if mes_atual == mes and dia_atual >= dia:
            contador += 1
    print(f'\n\n{contador}\n\n')

print(f'Quantidade de pessoas maior de idade: {contador}')


# DESAFIO 3
Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
num = 6
contador = 0
for age in range(num):
    x = int(input('DIGITE UM NÚMERO: '))
    if x % 2 == 0:
        contador += x
print(contador)


# DESAFIO 4
# Crie um programa que percorra uma certa quantidade de valores (mínimo 10) e exiba para o usuário apenas
# os números pares

valor = int(input('VALOR: '))
for x in range(0, valor, 2):
    print(f'{x}')


# DESAFIO 5
# Construa um programa que peça pro usuário digitar um número. Com base no valor digitado, verifique se
# atende a algum requisito e retorne o respectivo valor:
# ● Divisível por 3 = Fizz
# ● Divisível por 5 = Buzz
# ● Divisível por 3 e 5 = FizzBuzz
# ● Não atende nenhuma das condições acima, retorne o próprio número

value = int(input("Type a number:\n"))
f = ''
b = ''
if value % 3 == 0:
    f = 'Fizz'
if value % 5 ==0:
    b = 'Buzz'
print(f'{f}{b}')
if f == '' and b == '':
    print(value)


# DESAFIO 6
# Faça um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual valor a ser sacado (inteiro) e o programa vai
# informar quantas cédulas de cada valor serão entregues.
# Observação: considere que o caixa possui cédulas de R$ 1, R$ 10, R$ 20, R$ 50.

c50 = 0
c20 = 0
c10 = 0
c1 = 0
saque = int(input("QUE VALOR DESEJA SACAR?\n"))

if saque // 50 >= 1:
    c50 = saque // 50
    saque = saque % 50
if saque // 20 >= 1:
    c20 = saque // 20
    saque = saque % 20
if saque // 10 >= 1:
    c10 = saque // 10
    saque = saque % 10
    c1 = saque

print(F'''VOCÊ IRÁ RETIRAR:
{c50} NOTAS DE 50
{c20} NOTAS DE 20
{c10} NOTAS DE 10
{c1} MOEDAS DE 1''')



















import textwrap
import math
from cgitb import text

# DESAFIO 1
# text = input('Digite seu nome completo: ')
# print(f'Em maiúsculo: {text.upper()}')
# print(f'Em minúsculo: {text.lower()}')
# print(f'''Total de letras do seu nome com espaço: {len(text)}
# Sem espaço: {len(text.replace(" ", ""))}''')
# print(f'O total de letras do primeiro nome é: {text.find(" ")}')


# DESAFIO 2
# numero = input('Digite um número de 4 dígitos: ')
#
# if len(numero) == 4 and numero[0] != '0':
#     print(f'Número: {numero}')
#     print(f'Unidade: {numero[3]}')
#     print(f'Dezena: {numero[2]}')
#     print(f'Centena: {numero[1]}')
#     print(f'Milhar: {numero[0]}')
# else:
#     print('Erro')


# DESAFIO 3
# cidade = str(input('Digite o nome da sua cidade: ')).lower()
#
# if 'santo' in cidade:
#     print("True")
# else:
#     print("False")


# DESAFIO 4
# nome = str(input('Digite seu nome: ')).upper()
# print(nome[::-1])

# DESAFIO 5
ddd = input('Digite seu DDD: ')
if len(ddd) == 2:
    tel = input('Digite seu número: ')
    if len(tel) < 8:
        print('Erro')

    elif (tel[0] == '9' and len(tel) == 9):
         print(f'''Ok
({ddd}) {tel}''')

    elif len(tel) == 8:
        print(f'({ddd}) 9{tel}')

    elif len(tel) == 9 and tel[0] != '9':
        print(f'({ddd}) {tel.replace(tel[0],"9")}')
      

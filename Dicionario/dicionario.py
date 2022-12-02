import time

# cadastro = {'nome': 'João', 'idade': 21}
#cadastro = dict(nome='João', idade=21)
# print(cadastro)
# print(cadastro['nome'])
# print(cadastro['idade'])

# teste = []
# while True:
#     nome = input('Digite seu nome: ')
#     idade = int(input('Digite sua idade: '))
#
#     cadastro = dict(nome=nome, idade=idade)
#     teste.append(cadastro)
#     print(teste)

# teste = []
# for i in range(2):
#     nome = input('Digite seu nome: ')
#     idade = int(input('Digite sua idade: '))
#     cidade = int(input('Digite sua cidade: '))
#     cadastro = dict(nome=nome, idade=idade, cidade=cidade)
#     print(cadastro.keys())
#     print(cadastro.values())
#     print(cadastro.items())
#     for chave, valor in cadastro.items():
#         print(f'{chave}- {valor}')


# dicionario = dict()
# dicionario1 = {'palavra': 'Abacaxi', 'definicao': 'Fruta cítrica'}
# dicionario2 = {'palavra': 'Melancia', 'definicao': 'Fruta aquosa'}
# listaFrutas = []
# listaFrutas.append(dicionario1)
# listaFrutas.append(dicionario2)
# print(listaFrutas)
# for x, y in enumerate(listaFrutas):
#     print(x)
#     print(y['palavra'])
#     if y['palavra'] == 'Abacaxi':
#         print(y['definicao'])

frutas = {'abacaxi': 'abacaxi é uma fruta cítrica',
              'abacate': 'abacate tem uma barriguinha',
              'limão': 'se você tem limão, faça uma limonada'}

while True:
    usuario = input(f'Digite uma fruta:\n').lower().strip()
    if usuario not in frutas:
        print('Fruta não cadastrada!')
        cad = input(f'Deseja cadastrar? [s] ou [n]\n').lower()
        if cad == 's':
            descricao = input(f'Insira uma descrição pra ela:\n')
            frutas[usuario] = descricao
            print(f'Cadastrada')
            print("-"*50)
    else:
        print(frutas[usuario])
        break


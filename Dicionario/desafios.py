# DESAFIO 1-------------------------------------------------------------------------------------------------------------
# lista1 = [28, 34, 55, 41, 9, 71]
# primeiro = set(lista1)
# lista2 = [9, 31, 44, 74, 28, 56]
# segundo = set(lista2)
# print(primeiro - segundo)
# print(segundo - primeiro)
# print(primeiro | segundo)
# print(primeiro & segundo)

# DESAFIO 2-------------------------------------------------------------------------------------------------------------
# def removedor(valor):
#     print(valor)
#     while valor != []:
#         valor.pop()
#         print(valor)
#
#
# if __name__ == '__main__':
#     lista = [10, 20, 30, 40, 50]
#     removedor(lista)

# DESAFIO 3-------------------------------------------------------------------------------------------------------------
# lista1 = [10, 20, 30, 40, 50]
# primeira = set(lista1)
# lista2 = [100, 90, 80, 70, 60]
# segunda = set(lista2)
# if (primeira & segunda):
#     print('\nPossui valores repetidos')
#     print(f'Os valores repetidos são: {primeira & segunda}')
# else:
#     print('Não sossui valores repetidos')

# DESAFIO 4-------------------------------------------------------------------------------------------------------------
# Considere a frase:
# “Esse é um teste para medir meus conhecimentos em python”
# Construa um dicionário que armazenará a quantidade de vezes que
# cada letra aparece na frase

# frase = 'Esse é um teste para medir meus conhecimentos em python'
# dic = dict()
# for i in frase:
#     if dic.__contains__(i):
#         dic[i] = dic[i]+1
#     else:
#         dic[i] = 1
#
# dic = str(dic)
# dic = dic.replace('{', '')
# dic = dic.replace('}', '')
# dic = dic.replace("'", '')
# dic = dic.replace(': ', '=')
# dic = dic.replace(', ', '\n')
# dic = dic.replace(' ', 'ESPAÇO')
#
#
# print(dic)
# DESAFIO 5-------------------------------------------------------------------------------------------------------------
# dados1 = dict()
# lista1 = []
# print('APERTE ENTER PARA ADICIONAR MAIS CAMPOS E ENTER DUPLO PARA PREENCHER OS CAMPOS')
# while True:
#     campos = input(f'Digite um campo:\n').lower().strip()
#     if campos == '':
#         break
#     dados1[campos] = ""
#     # print(dados1)
# while True:
#     for x in dados1:
#         valor = input(f'Digite o {x}: ')
#         dados1[x] = valor
#     lista1.append(dados1)
#     decisao = input('Ok! Enter para adicionar mais dados:')
#     if decisao != '':
#         break
# def convert(lista1):
#     lista1 = str(lista1)
#     lista1 = lista1.replace(', ', '\n')
#     lista1 = lista1.replace('{', '')
#     lista1 = lista1.replace('}', '')
#     lista1 = lista1.replace("'", '')
#     lista1 = lista1.replace(':', '-->')
#     lista1 = lista1.replace(']', '')
#     lista1 = lista1.replace('[', '')
#     # lista1 = lista1.replace(' ', '')
#     print(lista1)

# if __name__ == '__main__':
#     convert(lista1)
# DESAFIO 5-------------------------------------------------------------------------------------------------------------

lista_usuarios = []
# add = dict(Nome='', Idade=0)
add = dict()

def menu():
    opcao = int(input(
        f'[1] - Adicionar Usuário\n'
        f'[2] - Listar Usuários\n'
        f'[3] - Pesquisar Usuário\n'
        f'[4] - Atualizar Usuário\n'
        f'[5] - Sair\n\n'
        f'Escolha a opção desejada: '))

    # TODO if == 1 // if == 1 faz os dois
    # TODO if ==1 // elif == 1 faz somente o primeiro if
    if opcao == 1:
        adicionar()

    elif opcao == 2:
        listar()

    elif opcao == 3:
        pesquisar()

    elif opcao == 4:
        atualizar()

    elif opcao == 5:
        sair()


def adicionar():
    while True:
        nome = input('Nome: ').lower()
        idade = int(input('Idade: '))

        add['Nome'] = nome
        add['Idade'] = idade
        lista_usuarios.append(add.copy())
        adicionado = int(input(
            f'\033[1;32mAdicionado!\n\nPara retornar ao menu principal insira [0]\nPara adicionar mais usuários insira [1]\n\033[0;0m'))

        if adicionado == 0:
            menu()
            break
        elif adicionado == 1:
            pass


def listar():
    lista = str(lista_usuarios)
    lista = lista.replace('[', '')
    lista = lista.replace(']', '')
    lista = lista.replace('{', '')
    lista = lista.replace('}, ', '\n\n')
    lista = lista.replace('}', '')
    lista = lista.replace("'", '')
    lista = lista.replace(', ', '\n')
    lista = lista.replace('Nome', '\033[1;31mNome\033[0;0m')
    lista = lista.replace('Idade', '\033[1;31mIdade\033[0;0m')
    print(lista)
    listado = int(input(f'\033[1;32mConcluído!\n\nPara retornar ao menu principal insira [0]\033[0;0m'))
    if listado == 0:
        return menu()


def pesquisar():
    while True:
        pesquisa = input('Qual usuário deseja pesquisar? ').lower().strip()
        lista_nomes = []

        for i, j in enumerate(lista_usuarios):
            for indice, chave in enumerate(j):
                if str(j[chave]).__contains__(pesquisa):
                    lista_nomes.append(j)

        print(lista_nomes)
        pesquisado = int(input(
            f'\033[1;32mConcluído!\n\nPara retornar ao menu principal insira [0]\nPara pesquisar mais usuários insira [1]\n\033[0;0m'))
        if pesquisado == 0:
            menu()
            break
        elif pesquisado == 1:
            pass


def atualizar():
    while True:
        pesquisa = input('Qual usuário deseja pesquisar? ').lower().strip()
        lista_nomes = []

        indice_lista = -1
        for i, j in enumerate(lista_usuarios):
            for indice, chave in enumerate(j):
                if str(j[chave]).__contains__(pesquisa):
                    indice_lista = i
                    lista_nomes.append(j)

        print(lista_nomes)
        if len(lista_nomes) > 1:
            print(
                f'Existem {len(lista_nomes)} registros com o termo pesquisado, informe o número do que você deseja atualizar: ')
            for i in lista_nomes:
                print(f'[{i}] - {lista_nomes[i]}')
            escolha = int(input('Digite o número desejado: '))
            lista_usuarios.remove(escolha)
            novo_nome = input('Digite o novo nome: ')
            nova_idade = int(input('Digite a nova idade: '))
            add['Nome'] = novo_nome
            add['Idade'] = nova_idade
            lista_usuarios.append(add.copy())

        elif len(lista_nomes) == 1:
            
            lista_usuarios.remove(indice_lista)
            novo_nome = input('Digite o novo nome: ')
            nova_idade = int(input('Digite a nova idade: '))
            add['Nome'] = novo_nome
            add['Idade'] = nova_idade
            lista_usuarios.append(add.copy())
        else:
            print("Não foram encontrados registros")

        atualizado = input(
            f'\033[1;32mConcluído!\n\nPara retornar ao menu principal insira [0]\nPara atualizar mais usuários insira [1]\n\033[0;0m')
        if atualizado == 0:
            menu()
            break
        elif atualizado == 1:
            pass


def sair():
    decisao = input(f'Deseja mesmo encerrar a sessão?\n[S]  [N]\n').upper()
    if decisao == 'S':
        print('Ok')
    elif decisao == 'N':
        return menu()


if __name__ == '__main__':
    menu()

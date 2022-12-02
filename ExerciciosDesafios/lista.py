import random

 # DESAFIO 1- Lista = maior e menor valor digitado e suas respectivas posições.
 lista = []
 for i in range(0, 5):
     numero = int(input("Digite um numero: "))
     lista.append(numero)
 print(f'''O menor: {min(lista)} na posição {lista.index(min(lista))}
 O maior: {max(lista)} na posição {lista.index(max(lista))}''')

 
# DESAFIO 2- Lista = vários valores em ordem crescente, tendo 'L' como break
 numeros=[]
 print("APERTE 'L' PARA MOSTRAR A LISTA")
 while True:
     valor = input('Digite um número: ').upper()
     if valor.isnumeric():
         valor = int(valor)
         if valor not in numeros:
             numeros.append(valor)
     elif valor == 'L':
         numeros.sort()
         print(f'Lista: {numeros}')
         break


# DESAFIO 3- Lista na ordem correta de inserção
 lista1 = []
 lista2 = []
 for i in range(0,5):
     nmrs = int(input('Digite 5 numeros: '))

     lista1.append(nmrs)

 tamanho = len(lista1)
 for x in range(0,tamanho):
     aux = min(lista1)
     lista2.append(aux)
     del lista1[lista1.index(aux)]

 print(lista2)

 lista = []
 for i in range(0,5):
     numero = int(input('Digite 5 numeros: '))

     if i == 0 or numero > lista[-1]:
         lista.append(numero)
     else:
         posicao = 0
         while posicao < len(lista):
             if numero <= len[posicao]:
                 lista.insert(posicao, numero)

            
# DESAFIO 4- Quantos números foram digitados, lista ordenada de forma decrescente e se valor 5 está ou não
 lista = []

 qntd = int(input('Digite quantos números deseja inserir na lista: '))

 for i in range(qntd):
     lista.append(int(input('Digite um número: ')))
 if 5 in lista:
     print('O 5 está na lista')

 lista.sort(reverse=True)
 print(lista)

 
# DESAFIO 5- Lista par impar
 lista = []
 par = []
 impar = []

 while True:
     numero = int(input("valor: "))
     lista.append(numero)
     if numero % 2 == 0:
         par.append(numero)
     else:
         impar.append(numero)

     escolha = input("Digite 'C' para 'continuar' e 'S' para 'sair': ").upper().strip()
     if escolha == 'S':
         break

 print(lista)
 print(f'Pares: {par}')
 print(f'Pares: {impar}')

 
# DESAFIO 6- MEGA SENA
 qntd = int(input("Quantos jogos da Mega Sena você quer gerar? "))

 lista = []

 contador = 1

 while True:
     lista.clear()
     while len(lista) !=6:
         aux = random.randint(1,60)
         if aux not in lista:
             lista.append(aux)
     print(f'O jogo {contador} é: {lista}')
     contador += 1
     if contador> qntd:
         break

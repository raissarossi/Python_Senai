import math
import random
# DESAFIO 1
 def somar(n1,n2):
     resultado = n1 + n2
     print(f"Resultado da soma é: {resultado}")

 def validarNumero(numero):
     if numero.isnumeric():
       return True
     else:
         return False
 n1 = input('Digite um número: ')
 if validarNumero(n1):
     n1= int(n1)
     n2 = input('Digite um número: ')
     if validarNumero(n2):
         n2= int(n1)
         somar(n1,n2)
     else:
         print('Insira um valor válido')

 else:
     print('Insira um valor válido')




 # DESAFIO 2
 n1 = input('digite um número: ')
 if validarNumero(n1):
     n1 = int(n1)
     n2 = input('digite outro número: ')
     if validarNumero(n2):
         n2 = int(n2)
         print(f"A soma é:",n1 + n2)
         print(f"A subtração é:",n1 - n2)
         print(f"A multiplicação é:",n1 * n2)
         print(f"A divisão é:",n1 / n2)
         print(f"A divisão inteira é:", n1 // n2)
         print(f"O resto da divisão é:", n1 % n2)
         print(f"A potência é:",n1 ** n2)
         print(f"As raizes são:",math.sqrt(n1),"e",math.sqrt(n2))


     else:
         print('digite um número inteiro')
else:
    print('digite um número inteiro')

# DESAFIO 3
x = random.randint(0,5)
ask = int(input('Qual número você pensou? '))
if ask == x:
   print('Você acertou')
if ask != x:
   print('Você errou, eu pensei em ',x,' e você em ',ask )

# DESAFIO 4

primeiro = float(input('Insira um número: '))
segundo = float(input('Insira outro número: '))
terceiro = float(input('Insira mais um número: '))

maior = primeiro
if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro
print("Maior é: ",maior)

menor = primeiro
if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro
print("Menor é: ",menor)



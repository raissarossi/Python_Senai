# import random

# DESAFIO 1
 def resposta():
     decisao = random.randint(1,2)
     if decisao == 1:
         print('Sim')
     elif decisao == 2:
         print ('Não')

 pergunta = input('''Faça uma pergunta de Sim ou Não:
 ''')
 resposta()

    
# DESAFIO 2
while True:
    frase = input('''Escreva uma frase palíndrome para verificarmos:
    ''')
    if str(frase) == str(frase)[::-1]:
        print("Palíndrome")
    else:
        print("Não é palíndrome")
        break

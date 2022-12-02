import threading

import veiculos; import status; import cidades;

nova_cidade = cidades.cidades()

# nova_cidade.exibir_cidades()
# marca = input("MARCA: ")
# modelo = input("MODELO: ")
# placa = input("PLACA: ")
consumo = input('CONSUMO (L/Km): ')
combustivel = input('NÍVEL DE COMBUSTÍVEL (em L): ')
continuar = True
mov = input('MOVIMENTO? [S] [N]\n').lower().strip()
vel = 0

if mov == 's':
    vel = int(input('VELOCIDADE:'))
    print('\n')
    situacao = status.status(movimento=mov, distancia=nova_cidade.destinos(distancia=0), velocidade=vel)

else:
    mov = input(f'Deseja ir pra algum lugar? [S] [N]').lower().strip()
    print('\n')
    if mov == 's':
        situacao = status.status(movimento=mov, distancia=nova_cidade.destinos(distancia=0), velocidade=vel)
    else:
        print('Até mais')
        continuar = False
if continuar:
    thread1 = threading.Thread(target=situacao.tempoEstimado)
    thread1.start()
    while True:
        situacao.acelerar()






if __name__ == '__main__':
    car = veiculos.carro
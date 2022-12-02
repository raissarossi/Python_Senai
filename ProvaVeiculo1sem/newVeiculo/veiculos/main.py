import threading

import veiculos; import status; import cidades;

nova_cidade = cidades.cidades()
consumo = input('CONSUMO (L/Km): ')
combustivel = input('NÍVEL DE COMBUSTÍVEL (em L): ')
situacao = status.status(movimento=False, distancia=nova_cidade.destinos(distancia=0), velocidade=0)

opcao = input("Iniciar corrida? [S] [N]").upper().strip()
if opcao == 'S':
	thread1 = threading.Thread(target=situacao.tempoEstimado)
	thread1.start()
else:
	print('Até mais')
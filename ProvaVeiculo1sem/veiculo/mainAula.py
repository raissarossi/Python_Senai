import threading; from Aula import IA; from aula1 import exibir


IA.distancia = 200
IA.velocidade = 80

info = exibir()
# info.atualizar()
thread1 = threading.Thread(target=info.atualizar).start()
thread123 = threading.Thread(target=info.atualizar).start()
print(f'Travou?')
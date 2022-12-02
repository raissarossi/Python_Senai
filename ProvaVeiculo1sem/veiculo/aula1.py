import time
# from Aula import IA

class IA:
    running = True
    distancia = 0
    velocidade = 0

class exibir:
    def atualizar(self):
        self.contador = 0
        while True:
            print(f'A distância atual é: {IA.distancia}')
            time.sleep(5)
            self.contador+=1
            if self.contador == 3:
                break
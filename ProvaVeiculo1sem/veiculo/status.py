import sys
import time

from cidades import cidades

class status:
    def __init__(self, movimento, velocidade, distancia):
        self.movimento = movimento
        self.distancia = distancia
        self.velocidade = velocidade
        print(self.movimento)
        print(self.distancia)
        print(self.velocidade)


    def tempoEstimado(self):
        while True:
            tempoPrevisto = self.distancia / self.velocidade
            # print(tempoPrevisto)
            horas = round(tempoPrevisto, 0)
            print("tempo",horas)
            time.sleep(2)

    def acelerar(self):
        self.velocidade

        opcao = int(input(f'''[1] - Acelerar
        [2] - Desacelerar'''))

        if opcao == 1:
            self.velocidade += 10
            print("velocidade atual ",self.velocidade)
        elif opcao == 2:
            self.velocidade -= 10
            print("velocidade atual ",self.velocidade)
        else:
            print("nao tenendi")

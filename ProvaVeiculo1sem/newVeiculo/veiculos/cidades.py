class cidades:

    def destinos(self, distancia):
        self.distancia = distancia
        global x
        self.cid = [
            {'cidade': 'Valinhos', 'num': 10},
            {'cidade': 'Campinas', 'num': 35},
            {'cidade': 'indaiatuba', 'num': 20},
            {'cidade': 'jaguariúna', 'num': 45},
            {'cidade': 'sumaré', 'num': 30},
            {'cidade': 'itatiba', 'num': 50},
            {'cidade': 'a', 'num': 20},
            {'cidade': 's', 'num': 50}
        ]

        while True:

            for x, y in enumerate(self.cid):
                print(f'[{x}] - {y["cidade"]} ')
            cidadeA = int(input(f'\033[1;36mQual cidade você está?\n\033[0;0m'))
            cA = self.cid[cidadeA]
            numA = cA['num']
            print(numA)
            break

            #
            # escolha = int(input('Escolha uma das cidades acima: '))

            # if cidadeA in cid:
            #     x = cid[cidadeA]['num']
            #     break
            # else:
            #     print("Cidade inválida")
            #     continue
        print('\n')
        while True:
            for x, y in enumerate(self.cid):
                print(f'[{x}] - {y["cidade"]} ')
            cidadeB = int(input(f'\033[1;36mPara qual cidade você pretende ir?\n\033[0;0m'))
            cB = self.cid[cidadeB]
            numB = cB['num']
            print(numB)
            break

            # if cidadeB in cid:
            #     y = cid[cidadeB]['num']
            #     break
            # else:
            #     print("Cidade inválida")

        self.distancia = numA+numB
        print(f'A distância é {self.distancia} KM')
        return self.distancia
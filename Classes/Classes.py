class Aluno:
    escola = "SENAI"

    def __init__(self, nome, nota, soma = 0, qntd = 0, ano = 2000):
        self.nome = nome
        self.ano = ano
        self.nota = nota
        self.soma = soma
        self.qntd = qntd

    def maior(self):
        if 2022 - self.ano >= 18:
            return True
        return False

    def calcula_media(self):
        media = self.soma/self.qntd
        return media

    def comparar_nota(self, media):
        if media >= 7:
            return f'Parabéns {self.nome} você foi aprovado!'
        return f'{self.nome} você foi rejeitado, estude mais!'

# Aluno.escola = 'SESI'
# aluno1 = Aluno('Luciano',2010)
# print(aluno1.maior())
# if aluno1.maior():
#     print('Chamar função pra aluno de maior')
# else:
#     print('Não foi possivel, volte ano que vem!')
# print(f'O {aluno1.nome} estuda no {aluno1.escola}')
#
# aluno2 = Aluno('João',1900)
# print(f'O {aluno2.nome} estuda no {aluno2.escola}')
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def getPreco(self):
        return self.preco

    def setPreco(self, preco):
        if preco < 0:
            raise ValueError('O PREÇO NAO PODE SER NEGATIVO')

# estudante = Aluno('nome', 0)
# lista = []
# while True:
#     nome = input("Digite seu nome:\n")
#     ano = int(input("Digite seu ano:\n"))
    # qntd = int(input('Quantas notas deseja inserir na média?\n'))
    # for i in range(qntd):
    #     lista.append(float(input("Insira sua nota:\n")))
    # soma = sum(lista)
    # estudante.soma = soma
    # estudante.qntd = qntd
    # estudante.nome = nome
    # estudante.ano = ano
    # estudante.nota = nota
    # res = estudante.calcula_media()
    # print(res)
    # print(estudante.comparar_nota(res))

    # if estudante.maior():
    #     print('Já pode tirar habilitação:)\n')
    # else:
    #     print('Não é maior de idade :(\n')



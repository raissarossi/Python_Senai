class Humano:
    nome = ''
    idade = 0
    sexo = ''

    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

class Aprendiz(Humano):
    def __init__(self, remuneracao_hora, nomeA):
        super.__init__(nome=nomeA,idade=idadeA,sexo=sexoA)
        self.remuneracao_hora = remuneracao_hora

class Gerente(Humano):
    def __init__(self, ferias, nomeG, idadeG, sexoG):
        super.__init__(nome=nomeG,idade=idadeG,sexo=sexoG)
        self.ferias = ferias

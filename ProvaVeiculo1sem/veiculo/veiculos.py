class veiculo:
    def __init__(self, marca, modelo, placa, consumo, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.consumo = consumo
        self.combustivel = combustivel

class carro(veiculo):
    def __init__(self, marca, modelo, placa, consumo, combustivel, categoria, airbags, portaMala, conversivel):
        super().__init__(marca, modelo, placa, consumo, combustivel)
        self.categoria = categoria
        self.airbags = airbags
        self.portaMala = portaMala
        self.conversivel = conversivel



class SenaiBank:
    agencia = 0
    def __init__(self, nome, cpf, idade):
            self.nome = nome
            self.cpf = cpf
            self.idade = idade
            self.__saldo = 1000
            self.__poupanca = 0


    def sacar(self, valor_sacar):
        if valor_sacar > self.__saldo:
            return False
        return True

    def efetivar_saque(self, valor_sacar):
        self.__saldo = self.__saldo - valor_sacar
        return self.__saldo

    def depositar(self, valor_depositar):
        self.__saldo = self.__saldo + valor_depositar
        return self.__saldo

    def transferir(self, valor_transf):
        self.__saldo = self.__saldo - valor_transf
        return self.__saldo

    def tranfP(self, valor_transf):
        self.__poupanca = self.__poupanca + valor_transf
        return self.__poupanca

    def extrato(self):
        return self.__saldo

    def extratoP(self):
        return self.__poupanca

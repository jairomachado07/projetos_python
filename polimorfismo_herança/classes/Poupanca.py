from classes.Conta import Conta

class Poupanca(Conta):
    def __init__(self, taxa_remuneracao):
        self.taxa_remuneracao = taxa_remuneracao

    def remuneraConta(self):
        self.saldo += self.saldo * self.taxa_remuneracao
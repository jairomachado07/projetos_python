
from classes.Extrato import Extrato
from datetime import datetime


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.movimentacoes.append(["Depósito", valor, datetime.now()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.movimentacoes.append(["Saque", valor, datetime.now()])
            return True

    def transferir(self, valor, conta_destino):
        if self.saldo < valor:
            return "Não existe saldo suficiente."
        else:
            conta_destino.depositar(valor)
            self.extrato.movimentacoes.append(["Transferência", valor, datetime.now()])
            self.saldo -= valor
        return "Transferência realizada com sucesso."
    
    def mostrar_saldo(self):
        print(f"numero: {self.numero}\nsaldo: {self.saldo}")


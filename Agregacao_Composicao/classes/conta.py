
from classes.Extrato import Extrato
import datetime


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.__clientes = clientes
        self.__numero = numero
        self.__saldo = saldo
        self.__data_abertura = datetime.datetime.today()
        self.__extrato = Extrato()

    def depositar(self, valor):
        self.__saldo += valor
        self.__extrato.movimentacoes.append(["Depósito", valor, datetime.datetime.now()])

    def sacar(self, valor):
        if self.__saldo < valor:
            return False
        else:
            self.__saldo -= valor
            self.__extrato.movimentacoes.append(["Saque", valor, datetime.datetime.now()])
            return True

    def transferir(self, valor, conta_destino):
        if self.__saldo < valor:
            return "Não existe saldo suficiente."
        else:
            conta_destino.depositar(valor)
            self.__extrato.movimentacoes.append(["Transferência", valor, datetime.datetime.now()])
            self.__saldo -= valor
        return "Transferência realizada com sucesso."
    
    def mostrar_saldo(self):
        print(f"numero: {self.__numero}\nsaldo: {self.__saldo}")


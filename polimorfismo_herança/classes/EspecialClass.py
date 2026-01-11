from classes.Conta import Conta
from datetime import datetime


class EspecialClass(Conta):
    
    def __init__(self, clientes, numero, saldo, limite):
        super().__init__(clientes, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print(f"Não existe saldo suficiente. Conta número: {self.numero} cliente: {self.clientes[0].cpf}")
            return False
        else:
            self.saldo -= valor
            self.extrato.movimentacoes.append(["Saque", valor, datetime.now()])
            return True
    
   

  
    
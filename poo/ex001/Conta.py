class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        return True

    def gerar_extrato(self):
        print(f"Numero: {self.numero}")
        print(f"CPF: {self.cpf}")
        print(f"Nome: {self.nomeTitular}")
        print(f"Saldo: {self.saldo}")

    def transferir(self, conta_destino, valor):
        if self.saldo < valor:
            return ("Saldo insuficiente")
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            return ("Transferência realizada com sucesso")
        
    def separador():
        print("-=-" * 20)

c1 = Conta(1, 123444321, "Guanabara", 1000)
c2 = Conta(2, 987654321, "Maria", 1000)

Conta.separador()
valor_saque = 1000
resultado_saque = c1.sacar(valor_saque)
print(c1.transferir(c2, 500))
Conta.separador()
c1.gerar_extrato()
Conta.separador()
c2.gerar_extrato()
Conta.separador()
from classes.ContaCliente import ContaCliente   

class Banco:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def adicionar_conta(self, conta_cliente):
        self.contas.append(conta_cliente)

    def calcular_rendimento(self):
        for conta in self.contas:
            conta.calcular_rendimento()

    def extrato(self):
        for conta in self.contas:
            conta.extrato()

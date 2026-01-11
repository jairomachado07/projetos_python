from classes.ContaCliente import ContaCliente


class ContaComum(ContaCliente):

    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        super().__init__(numero, IOF, IR, valor_investido, taxa_rendimento)

    def calcular_rendimento(self):
        remuneracao = self.valor_investido * self.taxa_rendimento
        valorIOF = remuneracao * self.IOF
        valorIR = remuneracao * self.IR
        self.valor_investido += remuneracao - valorIOF - valorIR

    def extrato(self):
        print(f"O saldo atual da conta {self.numero} é {self.valor_investido:10.2f}")

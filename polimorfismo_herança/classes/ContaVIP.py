from classes import ContaCliente

class ContaVIP(ContaCliente):
    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        super().__init__(numero, IOF, IR, valor_investido, taxa_rendimento)
        

    def calcular_rendimento(self):
        super().calcular_rendimento()
        self.valor_investido += self.valor_investido * self.taxa_rendimento



class Extrato:
    def __init__(self):
        self.movimentacoes = []

    def mostrar_extrato(self, conta):
        print(f"Extrato da conta {conta}:")
        for movimentacao in self.movimentacoes:
            print(f"{movimentacao[0]:15s}{movimentacao[1]:10.2f} {movimentacao[2].strftime('%d/%b/%Y')}")

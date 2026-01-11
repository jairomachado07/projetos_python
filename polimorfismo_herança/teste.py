import classes.Banco
from classes.ContaRemuneradaPoupanca import ContaRemuneradaPoupanca
from classes.ContaComum import ContaComum
from classes.ContaVIP import ContaVIP


banco1 = classes.Banco.Banco(999, "Teste")

conta_cliente1 = ContaCliente(1, 0.01, 0.15, 1000, 0.05)
conta_comum1 = ContaComum(2, 0.01, 0.15, 1000, 0.05)
conta_remunerada = ContaRemuneradaPoupanca(3, 0.01, 0.15, 1000, 0.05)

banco1.adicionar_conta(conta_cliente1)
banco1.adicionar_conta(conta_comum1)
banco1.adicionar_conta(conta_remunerada)

banco1.calcular_rendimento()
banco1.extrato()

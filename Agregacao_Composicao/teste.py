from classes.cliente import Cliente
from classes.conta import Conta

cliente1 = Cliente("12345678901", "João da Silva", "Rua A, 123")
cliente2 = Cliente("10987654321", "Maria Oliveira", "Rua B, 456")

conta1 = Conta([cliente1, cliente2], 100, 0)

conta1.depositar(500)
conta1.sacar(150)
conta1._Conta__extrato.mostrar_extrato(conta1._Conta__numero)
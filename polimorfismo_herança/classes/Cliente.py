from datetime import datetime
from classes.Extrato import Extrato


class Cliente:

    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.data_abertura = datetime.today()
        self.extrato = Extrato()
import datetime
from classes.Extrato import Extrato


class Cliente:

    def __init__(self, cpf, nome, endereco):
        self.__cpf = cpf
        self.__nome = nome
        self.__endereco = endereco
        self.__data_abertura = datetime.datetime.today()
        self.__extrato = Extrato()
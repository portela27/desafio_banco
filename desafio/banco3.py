from abc import ABC,abstractclassmethod,abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self,endereço) :
        self.endereço = endereço
        self.contas = []

    def re_transacao(self,conta,transacao):
        transacao.registrar(conta)

    def adicionar_conta (self,conta):
        self.contas.append(conta)


class Pessoa(Cliente):
    def __init__(self,nome,data_nasc,cpf,endereço):

        super().__init__(endereço)
        self.nome = nome
        self.data_nac = data_nasc
        self.cpf = cpf


class conta:
        def __init__(self,numero,cliente) :
             self._saldo = 0 
             self._numero = numero
             self._agencia = '0001'
             self._cliente = cliente
             self._historico = historico()

        @classmethod
        def nova_conta(cls,cliente,numero):
             return cls(numero,cliente)
        
        @property
        def saldo(self):
             return self._saldo
        
        @property
        def numero(self):
             return self._numero
       
        @property
        def agencia(self):
             return self._agencia
        
        @property
        def cliente(self):
             return self._cliente
        
        @property
        def historico(self):
             return self._historico
        
        def sacar(self,valor):
             saldo = self.saldo
             exedeu_saldo = valor > saldo

            
            if exedeu_saldo :
                print('operação falha ')

            elif valor > 0:
             self.saldo -= valor 
             print('bom saque ')
            return True

    

        


4- Crie uma classe para implementar uma conta corrente.
. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
. Os métodos são os seguintes: alterarNome, depósito e saque;
. No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios. 
. Faça um programa que simule um televisor criando-o como um objeto. 
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome
    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
        else:
            print("Saldo insuficiente. Operação não realizada.")
class Televisor:
    def __init__(self):
        self.canal = 1
        self.volume = 10
    def mudar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
            print(f"Canal alterado para {self.canal}")
        else:
            print("Canal inválido. Escolha um canal entre 1 e 100.")
    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}")
        else:
            print("Volume no máximo.")
    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}")
        else:
            print("Volume no mínimo.")
conta = ContaCorrente(123, "João da Silva")
conta.deposito(500)
conta.saque(200)
televisor = Televisor()
televisor.mudar_canal(5)
televisor.aumentar_volume()
televisor.diminuir_volume()
  


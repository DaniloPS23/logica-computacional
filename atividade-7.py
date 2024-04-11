Crie uma classe que modele um quadrado:

  Atributos: Tamanho do lado
  
  Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
  def __init__(self, lado):
   self.lado = lado
  def mudar_lado(self, novo_lado):
   self.novo_lado=novo_lado
  def retornar_lado(self):
   return self.lado
  def calcular_area(self):
   return self.lado**2
lado_inicial=float(input('insira o tamanho do lado desejado: '))

meu_quadrado=Quadrado(lado_inicial)

print(f"\nValor do lado: {meu_quadrado.retornar_lado()}")
novo_lado = float(input("Digite o novo valor do lado: "))
meu_quadrado.mudar_lado(novo_lado)

print(f"\nValor do lado atualizado: {meu_quadrado.retornar_lado()}")
print(f"Área do quadrado: {meu_quadrado.calcular_area()}")

 Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)

Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class retandulo:
  def __init__ (self,lado_A, lado_B):
   self.lado_A= lado_A
   self.lado_B= lado_B
  def mudar_lados(self, novo_lado_A, novo_lado_B):
   self.lado_A= novo_lado_A
   self.lado_B= novo_lado_B
  def retornar_lados(self):
    return self.lado_A, self.lado_B
  def calcular_area(self):
    return self.lado_A*self.lado_B
  def calcular_perimetro(self):
    return 2*(self.lado_A+self.lado_B)
base=float(input('insira a base: '))
altura=float(input('insira a altura: '))
local=retandulo(base, altura)
area_local=local.calcular_area()
perimetro_local=local.calcular_perimetro()
quantidade_pisos=area_local
quantidade_rodapes=perimetro_local

print(f"\nÁrea do local: {area_local:.0f} metros quadrados")
print(f"Perímetro do local: {perimetro_local:.0f} metros")
print(f"Quantidade de pisos necessários: {quantidade_pisos:.0f} peças")
print(f"Quantidade de rodapés necessários: {quantidade_rodapes:.0f} metros")

Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura

Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class pessoa():
 def __init__ (self,nome, peso, altura, idade):
  self.nome= nome
  self.peso= peso
  self.altura= altura
  self.idade= idade

 def envelhecer(self, anos):
  self.idade = self.idade + anos

 def engordar(self,quilos):
  self.peso += quilos

 def emagrecer(self, quilos):
  self.peso= self.peso - quilos

 def crescer(self, centimetros):
  if self.idade<=21:
    self.altura = self.idade*0.5

 def imprimir_informacoes(self):
        print(f"\nNome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} cm")



pessoa1 = pessoa("João", 18, 70, 170)


pessoa1.envelhecer(3)
pessoa1.engordar(5)
pessoa1.crescer(2)
pessoa1.imprimir_informacoes()

Crie uma classe para implementar uma conta corrente.

A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.

Os métodos são os seguintes: alterarNome, depósito e saque;

No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

 Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

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


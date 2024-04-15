1. Crie uma classe que modele uma pessoa
(a) Atributos: nome, idade e endereço
(b) Metodos: mostrar endereço e alterar endereço

class Pessoa:
  def __init__(self,nome, idade, endereco):
   self.nome= nome
   self.idade= idade
   self.endereco= endereco
  def mudar_endereco(self,novo_endereco):
   self.endereco= novo_endereco
  def retornar_endereco(self):
    print(self.endereco)
  def deletar_endereco(self):
    self.endereco=None
    idade=int(input('insira sua idade: '))
nome=str(input('insira seu nome: '))
endereco_inicial=str(input('insira seu endereco: '))
pessoa1=Pessoa(nome, idade, endereco_inicial)
print(pessoa1.nome)
print(pessoa1.endereco)
print(pessoa1.idade)
pessoa1.deletar_endereco()
pessoa1.mudar_endereco('rua 2')
pessoa1.retornar_endereco()

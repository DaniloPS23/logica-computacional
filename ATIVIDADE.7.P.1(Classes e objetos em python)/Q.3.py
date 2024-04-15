3- Crie uma classe que modele uma pessoa:
. Atributos: nome, idade, peso e altura
. Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

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

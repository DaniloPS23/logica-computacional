1- Crie uma classe que modele um quadrado:
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

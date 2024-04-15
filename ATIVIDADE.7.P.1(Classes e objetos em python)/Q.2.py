2-Crie uma classe que modele um retangulo:
. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
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

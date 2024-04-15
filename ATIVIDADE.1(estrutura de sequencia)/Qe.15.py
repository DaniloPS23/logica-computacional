15 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R 80,00ouemgalõesde3,6litros,quecustamR  25,00.Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
. comprar apenas latas de 18 litros;
. comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math
area_a_pintar = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
cobertura_por_litro = 6
litros_necessarios = area_a_pintar / cobertura_por_litro
tamanho_lata = 18
tamanho_galao = 3.6
latas_necessarias = math.ceil(litros_necessarios / tamanho_lata)
galoes_necessarios = math.ceil(litros_necessarios / tamanho_galao)
latas_misturadas = math.ceil((litros_necessarios * 1.1) / tamanho_lata)
galoes_misturados = math.ceil((litros_necessarios * 1.1) / tamanho_galao)
preco_latas = latas_necessarias * 80
preco_galoes = galoes_necessarios * 25
preco_misturado = (latas_misturadas // tamanho_lata) * 80 + (galoes_misturados // tamanho_galao) * 25
print(f"Situação 1 - Comprar apenas latas de 18 litros:")
print(f"Quantidade de latas necessárias: {latas_necessarias}")
print(f"Preço total: R$ {preco_latas:.2f}\n")
print(f"Situação 2 - Comprar apenas galões de 3,6 litros:")
print(f"Quantidade de galões necessários: {galoes_necessarios}")
print(f"Preço total: R$ {preco_galoes:.2f}\n")
print(f"Situação 3 - Misturar latas e galões para minimizar desperdício:")
print(f"Quantidade de latas necessárias: {latas_misturadas}")
print(f"Quantidade de galões necessários: {galoes_misturados}")
print(f"Preço total: R$ {preco_misturado:.2f}")

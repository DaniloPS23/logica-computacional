1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.

print("Alo mundo")

2 - Faça um Programa que peça um número e então mostre a mensagem .

numero= int(input("Digite um número: "))
print(f"o numero digitado foi {numero}")
print("Alo mundo")

3 - Faça um Programa que peça dois números e imprima a soma.


a=24
b=76

c= a+b
print(c)

4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1=float(input("digite a nota do 1°bimestre: "))
nota2=float(input("digite a nota do 2°bimestre: "))
nota3=float(input("digite a nota do 3°bimestre: "))
nota4=float(input("digite a nota do 4°bimestre: "))

MEDIA= (nota1 + nota2 + nota3 + nota4) /4

print(f"a media das notas é: {MEDIA}")



5 - Faça um Programa que converta metros para centímetros.

metros = float(input("digite a quantidaded metros: "))
centimetros = metros*100
print(f"{metros:.0f} metros e igual a {centimetros:.0f} centimetros")

6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

r=float(input('digite o raio do circulo:'))
a=3.14*r**2
print(f'o raio do circulo {r:.0f} em area é {a:.2f} m²')

7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.


lado = float(input("Digite o lado do quadrado: "))
area = lado ** 2
dobro_area = 2 * area
print(f"A área do quadrado com lado {lado} é: {area}")
print(f"O dobro da área é: {dobro_area}")


8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


valor_hora= float(input('quanto voce ganha: '))
horas_trabalho= float(input('quantas horas voce trabalha por mês: '))
salário_total= valor_hora*horas_trabalho
print(f"Seu salário total no mês é: R${salário_total:.2f}")


9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

fahrenheit=float(input('mostre a temperatura em fahrenheit: '))
celcius=5*((fahrenheit-32)/9)
print(f'a temperatura em celcius {celcius:.2f} °C')

10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celcius=float(input('mostre a temperatura em celcius: '))
fahrenheit=(celcius*9/5)+32
print(f'a temperautura em celcius é {fahrenheit:.1f} °F')

11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

o terceiro elevado ao cubo.

*   o produto do dobro do primeiro com metade do segundo .
*  a soma do triplo do primeiro com o terceiro.
*  o terceiro elevado ao cubo.



inteiro1=int(input('digite um numero inteiro: '))
inteiro2=int(input('digiteum numero inteiro: '))
real=float(input('digire um numero real: '))

resultado1=(2*inteiro1) * (inteiro2/2)
print(f'O produto do dobro do primeiro com metade do segundo é: {resultado1}')
resultado2=(3*inteiro1)+ real
print(f'A soma do triplo do primeiro com o terceiro é: {resultado2}')
resultado3=real**3
print(f'O terceiro elevado ao cubo é: {resultado3}')

12 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável  (peso de peixes) e calcule o excesso. Gravar na variável  a quantidade de quilos além do limite e na variável  o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.


peso_peixe = float(input('mostre o peso do peixe que pescou: '))
limite_peso = 50
if peso_peixe > limite_peso:
  excesso_peso=peso_peixe - limite_peso
  valor_multa=excesso_peso*4
  print(f'excesso de peso concedido em {excesso_peso:.2f} quilos')
  print(f'o valor da multa sera de R$ {valor_multa:.2f}')
else:
  print('o peso de seu peixe esta nas normas da empresa, não tera nenhuma multa')

13 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

*  salário bruto
*   quanto pagou ao INSS.
*  quanto pagou ao sindicato.
*   o salário líquido.

calcule os descontos e o salário líquido, conforme a fórmula abaixo:
+ Salário Bruto : R$ - IR (11%) : R$ - INSS (8%) : R$ - Sindicato ( 5%) : R$  = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.

valor_nota=float(input('quanto voce ganha por hora: '))
horas_trabalhadas=float(input('mostre o numero de horas trabalhadas por mês: '))
salario_bruto=valor_nota*horas_trabalhadas
ir=0.11*salario_bruto
inss=0.08*salario_bruto
sindicato=0.05*salario_bruto
salario_liquido=salario_bruto-ir-inss-sindicato
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto de IR (11%): R$ {ir:.2f}")
print(f"Desconto de INSS (8%): R$ {inss:.2f}")
print(f"Desconto de Sindicato (5%): R$ {sindicato:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")

14 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.**negrito**

import math
area_a_pintar = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
cobertura_por_litro = 3
litros_necessarios = area_a_pintar / cobertura_por_litro
tamanho_lata = 18
latas_necessarias = math.ceil(litros_necessarios / tamanho_lata)
preco_total = latas_necessarias * 80
print(f"Quantidade de latas de tinta necessárias: {latas_necessarias}")
print(f"Preço total: R$ {preco_total:.2f}")


15 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

*   comprar apenas latas de 18 litros;
*  comprar apenas galões de 3,6 litros;

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


16 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = float(input("Digite o tamanho do arquivo para download em MB: "))
velocidade_link = float(input("Digite a velocidade do link de Internet em Mbps: "))
tempo_download = (tamanho_arquivo / velocidade_link) * 60
print(f"O tempo aproximado de download do arquivo é: {tempo_download:.2f} minutos")

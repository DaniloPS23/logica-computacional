12 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar
uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável (peso de peixes) e calcule o
excesso. Gravar na variável a quantidade de quilos além do limite e na variável o valor da multa que João deverá pagar. Imprima os dados
do programa com as mensagens adequadas.

peso_peixe = float(input('mostre o peso do peixe que pescou: '))
limite_peso = 50
if peso_peixe > limite_peso:
  excesso_peso=peso_peixe - limite_peso
  valor_multa=excesso_peso*4
  print(f'excesso de peso concedido em {excesso_peso:.2f} quilos')
  print(f'o valor da multa sera de R$ {valor_multa:.2f}')
else:
  print('o peso de seu peixe esta nas normas da empresa, não tera nenhuma multa')

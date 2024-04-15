4 - Faça um programa que leia 5 números e informe o maior número.

Maior_numero= 0
for d in range(5):
    numero=float(input(f'digite o {d+1}° numero: '))
    if  numero > Maior_numero:
      Maior_numero = numero

print(f'O maior numero é : {Maior_numero:.0f}')

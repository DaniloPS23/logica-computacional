5 - Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
quantidade= 5
for x in range(quantidade):
  numero=float(input(f'digite o {x+1}° numero: '))
  soma =soma+numero
  media= (quantidade+soma)/3
  print(f'a soma dos numeros e: {soma:.0f}')
  print(f'a media dos numeros e: {media:.0f}')

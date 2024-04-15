2 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

vetor=[]
for r in range(10):
   numero= int(input("digite um numero inteiro: "))
   vetor.append(numero)
   soma= sum(r ** 2  for r in vetor )
   print(f'a soma quadratica é: {soma}')

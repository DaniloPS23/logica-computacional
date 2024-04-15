5 - Faça um Programa que leia três números e mostre o maior deles.

N1=float(input('digite um primeiro numero: '))
N2=float(input('digite um segundo numero: '))
N3=float(input('digite um terceiro numero: '))
maior_numero= max(N1, N2, N3)
print(f'O maior entre esses numeros é: {maior_numero:.0f}')

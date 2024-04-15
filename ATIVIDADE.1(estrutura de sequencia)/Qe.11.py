11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o terceiro elevado ao cubo.
1- o produto do dobro do primeiro com metade do segundo .
2- a soma do triplo do primeiro com o terceiro.
3- o terceiro elevado ao cubo.

inteiro1=int(input('digite um numero inteiro: '))
inteiro2=int(input('digiteum numero inteiro: '))
real=float(input('digire um numero real: '))
resultado1=(2*inteiro1) * (inteiro2/2)
print(f'O produto do dobro do primeiro com metade do segundo é: {resultado1}')
resultado2=(3*inteiro1)+ real
print(f'A soma do triplo do primeiro com o terceiro é: {resultado2}')
resultado3=real**3
print(f'O terceiro elevado ao cubo é: {resultado3}')

7 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles. 
Altere o programa anterior para mostrar no final a soma dos números.

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
if numero1 > numero2:
    numero1, numero2 = numero2, numero1
soma = 0
print(f"Números no intervalo de {numero1} a {numero2}:")
for numero in range(numero1, numero2 + 1):
    print(numero, end=" ")
    soma += numero
print(f"\nSoma dos números no intervalo: {soma}")  

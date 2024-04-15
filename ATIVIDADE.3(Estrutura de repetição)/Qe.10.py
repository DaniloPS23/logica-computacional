10 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

quantidade_pares = 0
quantidade_impares = 0
for t in range(10):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        quantidade_pares += 1
    else:
        quantidade_impares += 1
print(f"\nQuantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")

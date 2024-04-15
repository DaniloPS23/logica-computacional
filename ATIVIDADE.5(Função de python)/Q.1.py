1 - Faça um programa para imprimir: 1 2 2 3 3 3 ..... n n n n n n ... n
para um informado pelo usuário. Use uma função que receba um valor inteiro e imprima até a n-ésima linha.

def imprimir_padrao2(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()
n = int(input("Digite o valor de n: "))
imprimir_padrao2(n)

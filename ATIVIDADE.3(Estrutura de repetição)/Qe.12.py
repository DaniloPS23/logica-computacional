12 - A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

termo1 = 0
termo2 = 1
print("Série de Fibonacci:")
print(termo1)
print(termo2)
while termo2 <= 500:
    proximo_termo = termo1 + termo2
    print(proximo_termo)
    termo1, termo2 = termo2, proximo_termo

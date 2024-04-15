9 - Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.

base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = 1
for _ in range(expoente):
    resultado = base * expoente
print(f"{base:.0f} elevado a {expoente:.0f} é igual a {resultado:.0f}")

3 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, 
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor1 = []
vetor2 = []
print("Digite os elementos para o primeiro vetor:")
for _ in range(10):
    elemento1 = int(input("Digite um elemento: "))
    vetor1.append(elemento1)
print("\nDigite os elementos para o segundo vetor:")
for _ in range(10):
    elemento2 = int(input("Digite um elemento: "))
    vetor2.append(elemento2)
vetor3 = []
for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
print("\nTerceiro vetor intercalado:")
print(vetor3)

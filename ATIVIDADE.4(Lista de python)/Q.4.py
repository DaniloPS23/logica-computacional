4 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor1 = []
vetor2 = []
vetor3 = []
print("Digite os elementos para o primeiro vetor:")
for _ in range(10):
    elemento1 = int(input("Digite um elemento: "))
    vetor1.append(elemento1)
print("\nDigite os elementos para o segundo vetor:")
for _ in range(10):
    elemento2 = int(input("Digite um elemento: "))
    vetor2.append(elemento2)
print("\nDigite os elementos para o terceiro vetor:")
for _ in range(10):
    elemento3 = int(input("Digite um elemento: "))
    vetor3.append(elemento3)
vetor4 = []
for i in range(10):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])
print("\nQuarto vetor intercalado:")
print(vetor4)

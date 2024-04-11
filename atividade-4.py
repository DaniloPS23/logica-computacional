1 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.


1altura=[]
idade=[]
x=0
while x<5:
  a=input('digite sua altura: ')
  i=input('digite sua idade: ')
  altura.append(a)
  idade.append(i)
  x=x+1
print(altura)
print(idade)



y=4
while y>=0:
  print('idade: ', idade[y], 'altura: ', altura[y])
  y=y-1

2 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

vetor=[]
for r in range(10):
   numero= int(input("digite um numero inteiro: "))
   vetor.append(numero)
   soma= sum(r ** 2  for r in vetor )
   print(f'a soma quadratica é: {soma}')




3 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.


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
4
print("\nTerceiro vetor intercalado:")
print(vetor3)


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


5 - Foram anotadas as idades e alturas de 10 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.


idades = []
alturas = []

for i in range(10):
    idade = int(input(f"Digite a idade do aluno {i + 1}: "))
    altura = float(input(f"Digite a altura do aluno {i + 1} (em metros): "))

    idades.append(idade)
    alturas.append(altura)

media_alturas = sum(alturas) / len(alturas)

alunos_mais_de_13 = sum(1 for i in range(10) if idades[i] > 13 and alturas[i] < media_alturas)
1.
print(f"\nQuantidade de alunos com mais de 13 anos e altura inferior à média: {alunos_mais_de_13}")

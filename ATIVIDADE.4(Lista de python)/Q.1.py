1 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.

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

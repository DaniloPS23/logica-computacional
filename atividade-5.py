1 - Faça um programa para imprimir:
1
 2 2
 3 3 3
.....
 n n n n n n ... n


para um  informado pelo usuário. Use uma função que receba um valor  inteiro e imprima até a n-ésima linha.

def imprimir_padrao(n):
    for i in range(1, n + 1):
        print((str(i) + ' ') * i)

# Teste
n = int(input("Digite o valor de n: "))
imprimir_padrao(n)


def imprimir_padrao2(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()

# Teste
n = int(input("Digite o valor de n: "))
imprimir_padrao2(n)

2 - Escreva uma função chamada fatorial que calcula o fatorial de um número inteiro fornecido como argumento.3 - Escreva uma função chamada verifica_primo que verifica se um número é primo ou não e retorna True ou False.


def fatorial(numero):
   if numero < 0:
    return
   elif numero == 0 or numero ==1:
     return 1
   else:
      resultado = 1
      for i in range(2,numero+1):
         resultado *= i
      return resultado
numero = int(input('insira um numero para calcular sua fatorial: '))
resultado_fatorial= fatorial(numero)
print(f'o numero que foi inserido {numero} tem sua fatorial  é {resultado_fatorial}')

def primo(numero):
 if numero > 2:
  for i in range(2,int(numero**0,5)+1):
    if numero % i == 0:
      return False
    return True
numero = int(input('digite um numero para saber se este numero e primo ou não: '))
def primo(numero):
  if numero <= 1:
    return False
  for i in range(2, numero):
    if numero % i == 0:
      return False
  return True
if primo(numero):
  print(f'esse numero e primo: {numero}')
else:
  print(f'esse numero não e um primo: {numero}')


3 - Escreva uma função chamada inverte_string que aceita uma string como parâmetro e retorna a string invertida.

def inverte_string(s):
  return s[::-1]
original= input('estreva uma pavavra para ser invertida: ')
invertida=inverte_string(original)
print(f'esse e a string originalmente: {original}')
print(f'esse e a string invertida: {invertida}')

4 - Escreva uma função chamada maior_valor que aceita uma lista de números como parâmetro e retorna o maior valor na lista.


def maior_valor(lista):
 if not lista:
   return
 else:
  return max(lista)
numeros=[2, 7, 5, 7, 6, 9, 3]
resultado=maior_valor(numeros)
print(f'o maoir valor corespondido é: {resultado}')

 5- Escreva uma função chamada conta_vogais que aceita uma string como parâmetro e retorna o número de vogais na string.

def conta_vogais(s):
  vogais='aeiouAEIOU'
  return sum(1 for char in s if char in vogais)
string=input('insira uma palavra para saber quais sao suas vogais: ')
resultado=conta_vogais(string)
print(f' o numero de vogais é: {resultado}')



6 - Escreva uma função chamada soma_quadrados que aceita uma lista de números como parâmetro e retorna a soma dos quadrados desses números.

def soma_quadrados(lista):
    return sum(x**2 for x in lista)

# Exemplo de uso
numeros = [2, 3, 4, 5]
resultado = soma_quadrados(numeros)
print(f"A soma dos quadrados dos números na lista é: {resultado}")


7 - Escreva uma função chamada imprime_tabuada que aceita um número inteiro como parâmetro e imprime a tabuada desse número de 1 a 10.

def imprime_tabuada(numero):
    print(f"Tabuada de {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")
numero = int(input("Digite um número inteiro para imprimir a tabuada: "))
imprime_tabuada(numero)

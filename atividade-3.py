1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota =float(input('digite a nota do aluno: '))
while nota<0 or nota>10:
  print('numero invalifo')
  nota =float(input('digite a nota do aluno: '))

2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.


usuario=input('digite um nome do usuario: ')
senha=input('digite a senha: ')
if senha == usuario:
  print('ouve um erro em sua descrição,por favor sertifique que sua senha ou usuario estajam corretos')
else:
  print('seu cadastro foi finalizado com sucesso')


3 - Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

for s in (1,20):
 print(s)
for s in range(1, 21):
    print(s, end=" ")

4 - Faça um programa que leia 5 números e informe o maior número.


Maior_numero= 0
for d in range(5):
    numero=float(input(f'digite o {d+1}° numero: '))
    if  numero > Maior_numero:
      Maior_numero = numero

print(f'O maior numero é : {Maior_numero:.0f}')


5 - Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
quantidade= 5
for x in range(quantidade):
  numero=float(input(f'digite o {x+1}° numero: '))
  soma =soma+numero
  media= (quantidade+soma)/3
  print(f'a soma dos numeros e: {soma:.0f}')
  print(f'a media dos numeros e: {media:.0f}')

6 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

for i in range (1,50):
  if i%2 > 0:
    print(i)

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


8 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50


numero=int(input('digite um numero de(1 a 10) para uma tabuada: '))
if 1 <= numero >= 10:
    print(f'\ntabuada de{numero}')
for x in range (1,10):
    resultado = numero * x
    print(f'{numero} X {x} = {resultado}')



9 - Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.


base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = 1
for _ in range(expoente):
    resultado = base * expoente
print(f"{base:.0f} elevado a {expoente:.0f} é igual a {resultado:.0f}")


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


11 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.


n = int(input("Digite o valor de n para gerar a série de Fibonacci: "))
fibonacci = [1, 1]
for i in range(2, n):
    proximo_termo = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(proximo_termo)
print(f"\nSérie de Fibonacci até o {n}º termo:")
for termo in fibonacci:
    print(termo, end=" ")


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


13 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

def main():
    numero = int(input("Digite um número inteiro para calcular o fatorial: "))
    if numero < 0:
        print("O fatorial de números negativos não é definido.")
    else:
        resultado = calcular_fatorial(numero)
        print(f"O fatorial de {numero} é: {resultado}")

if __name__ == "__main__":
    main()

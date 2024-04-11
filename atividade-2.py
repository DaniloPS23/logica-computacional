1 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor=float(input('digite um numero: '))
if valor > 0:
 print('O valor e positivo')
elif valor<0:
  print('O valor e negativo')
else:
  print('o valor e zero')

valor=float(input('digite um numero: '))
if valor > 0:
 print('O valor e positivo')
elif valor<0:
  print('O valor e negativo')
else:
  print('o valor e zero')

valor=float(input('digite um numero: '))
if valor > 0:
 print('O valor e positivo')
elif valor<0:
  print('O valor e negativo')
else:
  print('o valor e zero')

2 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


letra=input('digite uma letra(F OU M): ')
if letra.upper() == 'F':
  print('F de feminino')
elif letra.upper() == 'M':
  print('M de masculido')
else:
  print('não coresponde com um dos generos escolhidos')

letra=input('digite uma letra(F OU M): ')
if letra.upper() == 'F':
  print('F de feminino')
elif letra.upper() == 'M':
  print('M de masculido')
else:
  print('não coresponde com um dos generos escolhidos')

letra=input('digite uma letra(F OU M): ')
if letra.upper() == 'F':
  print('F de feminino')
elif letra.upper() == 'M':
  print('M de masculido')
else:
  print('não coresponde com um dos generos escolhidos')

3 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra=input('digite uma letra e verifique se e (vogal ou consoante) : ')
if letra.lower() in ['a','e','i','o','u'] :
 print('A letra correspondida é uma vogal')
else:
  print('a letra correspondida é uma consoante')


letra=input('digite uma letra e verifique se e (vogal ou consoante) : ')
if letra.lower() in ['a','e','i','o','u'] :
 print('A letra correspondida é uma vogal')
else:
  print('a letra correspondida é uma consoante')


4 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.


*  A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
*   A mensagem "Reprovado", se a média for menor do que sete;
*  A mensagem "Aprovado com Distinção", se a média for igual a dez.



nota1=float(input('digite a primeira nota: '))
nota2=float(input('digite a segunda nota: '))
media=(nota1+nota2)/2
if media == 10:
 print('exelente,voce pasou')
elif media >= 7:
 print('muito bem ,voce pasou')
else:
  print('sinto muito,vejo voce na recuperação')

nota1=float(input('digite a primeira nota: '))
nota2=float(input('digite a segunda nota: '))
media=(nota1+nota2)/2
if media == 10:
 print('exelente,voce pasou')
elif media >= 7:
 print('muito bem ,voce pasou')
else:
  print('sinto muito,vejo voce na recuperação')

nota1=float(input('digite a primeira nota: '))
nota2=float(input('digite a segunda nota: '))
media=(nota1+nota2)/2
if media == 10:
 print('exelente,voce pasou')
elif media >= 7:
 print('muito bem ,voce pasou')
else:
  print('sinto muito,vejo voce na recuperação')

5 - Faça um Programa que leia três números e mostre o maior deles.

N1=float(input('digite um primeiro numero: '))
N2=float(input('digite um segundo numero: '))
N3=float(input('digite um terceiro numero: '))
maior_numero= max(N1, N2, N3)
print(f'O maior entre esses numeros é: {maior_numero:.0f}')


6 - Faça um Programa que leia três números e mostre o maior e o menor deles.

N1=float(input('digite um primeiro numero: '))
N2=float(input('digite um segundo numero: '))
N3=float(input('digite um terceiro numero: '))
maior_numero= max(N1, N2, N3)
menor_numero= min(N1, N2, N3)
print(f'O maior entre esses numeros é: {maior_numero:.0f}')
print(f'o menor entre esses numeros é: {menor_numero:.0f}')

7 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco_do_produto1=float(input('mostre o preco do primeiro produto: '))
preco_do_produto2=float(input('mostre o preco do segundo produto: '))
preco_do_produto3=float(input('mostre o preco do terceiro produto: '))
produto_mais_barato= min(preco_do_produto1, preco_do_produto2, preco_do_produto3)
print(f'o produto mais barato possivel e o de: R${produto_mais_barato:.2f}')

8 - Faça um Programa que leia três números e mostre-os em ordem decrescente.



numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
numeros = [numero1, numero2, numero3]
numeros_ordem_decrescente = sorted(numeros, reverse=True)
print("Números em ordem decrescente:", numeros_ordem_decrescente)


9 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

*   salários até R$ 280,00 (incluindo) : aumento de 20%

*   salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
*   salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
*  salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
*  o salário antes do reajuste;
*   o percentual de aumento aplicado;
*  o valor do aumento;
*   o valor do aumento;





salario_atual = float(input("Digite o salário atual do colaborador: "))
if salario_atual <= 280:
    percentual_aumento = 20
elif salario_atual <= 700:
    percentual_aumento = 15
elif salario_atual <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5
aumento = (percentual_aumento / 100) * salario_atual
novo_salario = salario_atual + aumento
print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")


10 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:

*   Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
*   Triângulo Equilátero: três lados iguais;
*  Triângulo Isósceles: quaisquer dois lados iguais;
*   Triângulo Escaleno: três lados diferentes;




lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        tipo_triangulo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo_triangulo = "Isósceles"
    else:
        tipo_triangulo = "Escaleno"
    print(f"Os lados formam um triângulo {tipo_triangulo}.")
else:
    print("Os lados fornecidos não formam um triângulo.")

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        tipo_triangulo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo_triangulo = "Isósceles"
    else:
        tipo_triangulo = "Escaleno"
    print(f"Os lados formam um triângulo {tipo_triangulo}.")
else:
    print("Os lados fornecidos não formam um triângulo.")

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        tipo_triangulo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo_triangulo = "Isósceles"
    else:
        tipo_triangulo = "Escaleno"
    print(f"Os lados formam um triângulo {tipo_triangulo}.")
else:
    print("Os lados fornecidos não formam um triângulo.")

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        tipo_triangulo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo_triangulo = "Isósceles"
    else:
        tipo_triangulo = "Escaleno"
    print(f"Os lados formam um triângulo {tipo_triangulo}.")
else:
    print("Os lados fornecidos não formam um triângulo.")

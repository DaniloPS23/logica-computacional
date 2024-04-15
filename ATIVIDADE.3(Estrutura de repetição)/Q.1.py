1 - Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota =float(input('digite a nota do aluno: '))
while nota<0 or nota>10:
  print('numero invalifo')
  nota =float(input('digite a nota do aluno: '))

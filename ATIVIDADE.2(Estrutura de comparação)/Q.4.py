4 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno apresentar: A mensagem "Aprovado", 
se a média alcançada for maior ou igual a sete; A mensagem "Reprovado", se a média for menor do que sete; A mensagem "Aprovado com Distinção", 
se a média for igual a dez.
. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
. A mensagem "Reprovado", se a média for menor do que sete;
. A mensagem "Aprovado com Distinção", se a média for igual a dez.

  nota1=float(input('digite a primeira nota: '))
nota2=float(input('digite a segunda nota: '))
media=(nota1+nota2)/2
if media == 10:
 print('exelente,voce pasou')
elif media >= 7:
 print('muito bem ,voce pasou')
else:
  print('sinto muito,vejo voce na recuperação')

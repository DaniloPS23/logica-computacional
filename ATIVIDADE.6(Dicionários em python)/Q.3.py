3. Faça um programa, utilizando Dicionários, que peça para o usuário inserir quatro notas e mostre na tela as notas e a média entre elas.

  media={}
for x in range(1, 5):
  nota = float(input(f"insira uma nota {x}: "))
  notas_aluno[f'nota_{x}']= nota
  notas_media = sum(notas_aluno.values()) / len(notas_aluno)
print("\n nota do aluno: ")
for chave, valor in notas_aluno.items():
   print(f'{chave}: {valor}')
print(f'\nMédia das notas: {notas_media}')

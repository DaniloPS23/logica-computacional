1. Faça um programa que possua um Dicionário, adicione elementos ao dicionário e os mostre na tela.

meu_dicionario={}
meu_dicionario['nome']= 'Beatriz'
meu_dicionario['idade']= 34
meu_dicionario['profição'] = 'medica'
print('dicionario atualizado:')
for chave, valor in meu_dicionario.items():
  print(f'{chave}: {valor}')

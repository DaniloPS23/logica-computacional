2 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra=input('digite uma letra(F OU M): ')
if letra.upper() == 'F':
  print('F de feminino')
elif letra.upper() == 'M':
  print('M de masculido')
else:
  print('não coresponde com um dos generos escolhidos')

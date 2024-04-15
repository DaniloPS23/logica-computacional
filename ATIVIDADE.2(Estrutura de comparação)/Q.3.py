3 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra=input('digite uma letra e verifique se e (vogal ou consoante) : ')
if letra.lower() in ['a','e','i','o','u'] :
 print('A letra correspondida é uma vogal')
else:
  print('a letra correspondida é uma consoante')

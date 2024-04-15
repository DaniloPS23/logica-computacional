2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.

usuario=input('digite um nome do usuario: ')
senha=input('digite a senha: ')
if senha == usuario:
  print('ouve um erro em sua descrição,por favor sertifique que sua senha ou usuario estajam corretos')
else:
  print('seu cadastro foi finalizado com sucesso')

2. Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos de mercado e seus respectivos preços e os mostre na tela.

mercado={}
for i in range(3):
 produto=input('insira um nome de um produto: ')
 preco=float(input('insira um preço para o produto: '))
 mercado[produto]=preco
for produto, preco in mercado.items():
 print(f'{produto}:R$ {preco:.2f}')

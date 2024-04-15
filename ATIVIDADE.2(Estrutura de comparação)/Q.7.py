7 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre 
pelo mais barato.

preco_do_produto1=float(input('mostre o preco do primeiro produto: '))
preco_do_produto2=float(input('mostre o preco do segundo produto: '))
preco_do_produto3=float(input('mostre o preco do terceiro produto: '))
produto_mais_barato= min(preco_do_produto1, preco_do_produto2, preco_do_produto3)
print(f'o produto mais barato possivel e o de: R${produto_mais_barato:.2f}')

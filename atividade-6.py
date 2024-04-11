
1. Faça um programa que possua um Dicionário, adicione elementos ao dicionário e os mostre na tela.

meu_dicionario={}

meu_dicionario['nome']= 'Beatriz'
meu_dicionario['idade']= 34
meu_dicionario['profição'] = 'medica'
print('dicionario atualizado:')
for chave, valor in meu_dicionario.items():
  print(f'{chave}: {valor}')

2. Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos de mercado e seus respectivos preços e os mostre na tela.

mercado={}
for i in range(3):
 produto=input('insira um nome de um produto: ')
 preco=float(input('insira um preço para o produto: '))
 mercado[produto]=preco
for produto, preco in mercado.items():
 print(f'{produto}:R$ {preco:.2f}')


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

4. Faça um programa, utilizando Dicionários, que:

1° Passo: Peça para o usuário inserir quatro coisas em uma “Caixa Misteriosa” .

2° Passo: Peça para o usuário inserir um número.

3° Passo: Mostre na tela o que foi inserido na posição do número inserido pelo usuário.

def main():
    # Passo 1: Pedir ao usuário para inserir quatro coisas na "Caixa Misteriosa"
    caixa_misteriosa = {}
    for i in range(4):
        item = input(f"Insira o {i+1}º item na Caixa Misteriosa: ")
        caixa_misteriosa[i+1] = item
    
    # Passo 2: Pedir ao usuário para inserir um número
    numero = int(input("Insira um número de 1 a 4 para escolher um item da Caixa Misteriosa: "))
    
    # Passo 3: Mostrar na tela o que foi inserido na posição do número inserido pelo usuário
    if numero in caixa_misteriosa:
        print(f"Você escolheu o número {numero}. O item na Caixa Misteriosa nessa posição é: {caixa_misteriosa[numero]}")
    else:
        print("Número inválido. Por favor, insira um número de 1 a 4.")

if __name__ == "__main__":
    main()

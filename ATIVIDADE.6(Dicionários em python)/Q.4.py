4. Faça um programa, utilizando Dicionários, que:
1° Passo: Peça para o usuário inserir quatro coisas em uma “Caixa Misteriosa” .
2° Passo: Peça para o usuário inserir um número.
3° Passo: Mostre na tela o que foi inserido na posição do número inserido pelo usuário.

def main():
    caixa_misteriosa = {}
    for i in range(4):
        item = input(f"Insira o {i+1}º item na Caixa Misteriosa: ")
        caixa_misteriosa[i+1] = item
    numero = int(input("Insira um número de 1 a 4 para escolher um item da Caixa Misteriosa: "))
    if numero in caixa_misteriosa:
        print(f"Você escolheu o número {numero}. O item na Caixa Misteriosa nessa posição é: {caixa_misteriosa[numero]}")
    else:
        print("Número inválido. Por favor, insira um número de 1 a 4.")
if __name__ == "__main__":
    main()

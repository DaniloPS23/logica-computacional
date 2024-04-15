7 - Escreva uma função chamada imprime_tabuada que aceita um número inteiro como parâmetro e imprime a tabuada desse número de 1 a 10.

def imprime_tabuada(numero):
    print(f"Tabuada de {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")
numero = int(input("Digite um número inteiro para imprimir a tabuada: "))
imprime_tabuada(numero)

6 - Escreva uma função chamada soma_quadrados que aceita uma lista de números como parâmetro e retorna a soma dos quadrados desses números

def soma_quadrados(lista):
    return sum(x**2 for x in lista)
numeros = [2, 3, 4, 5]
resultado = soma_quadrados(numeros)
print(f"A soma dos quadrados dos números na lista é: {resultado}")

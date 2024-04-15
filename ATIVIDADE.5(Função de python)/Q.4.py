4 - Escreva uma função chamada maior_valor que aceita uma lista de números como parâmetro e retorna o maior valor na lista.

def maior_valor(lista):
 if not lista:
   return
 else:
  return max(lista)
numeros=[2, 7, 5, 7, 6, 9, 3]
resultado=maior_valor(numeros)
print(f'o maoir valor corespondido é: {resultado}')

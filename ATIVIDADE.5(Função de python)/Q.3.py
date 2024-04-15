3 - Escreva uma função chamada inverte_string que aceita uma string como parâmetro e retorna a string invertida.

def inverte_string(s):
  return s[::-1]
original= input('estreva uma pavavra para ser invertida: ')
invertida=inverte_string(original)
print(f'esse e a string originalmente: {original}')
print(f'esse e a string invertida: {invertida}')

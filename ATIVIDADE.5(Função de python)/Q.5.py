5- Escreva uma função chamada conta_vogais que aceita uma string como parâmetro e retorna o número de vogais na string.

  def conta_vogais(s):
  vogais='aeiouAEIOU'
  return sum(1 for char in s if char in vogais)
string=input('insira uma palavra para saber quais sao suas vogais: ')
resultado=conta_vogais(string)
print(f' o numero de vogais é: {resultado}')

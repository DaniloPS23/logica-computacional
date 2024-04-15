2 - Escreva uma função chamada fatorial que calcula o fatorial de um número inteiro fornecido como argumento.
2.1 - Escreva uma função chamada verifica_primo que verifica se um número é primo ou não e retorna True ou False.

  def fatorial(numero):
   if numero < 0:
    return
   elif numero == 0 or numero ==1:
     return 1
   else:
      resultado = 1
      for i in range(2,numero+1):
         resultado *= i
      return resultado
numero = int(input('insira um numero para calcular sua fatorial: '))
resultado_fatorial= fatorial(numero)
print(f'o numero que foi inserido {numero} tem sua fatorial  é {resultado_fatorial}')

def primo(numero):
 if numero > 2:
  for i in range(2,int(numero**0,5)+1):
    if numero % i == 0:
      return False
    return True
numero = int(input('digite um numero para saber se este numero e primo ou não: '))
def primo(numero):
  if numero <= 1:
    return False
  for i in range(2, numero):
    if numero % i == 0:
      return False
  return True
if primo(numero):
  print(f'esse numero e primo: {numero}')
else:
  print(f'esse numero não e um primo: {numero}')

8 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada.
A saída deve ser conforme o exemplo abaixo:

Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50

numero=int(input('digite um numero de(1 a 10) para uma tabuada: '))
if 1 <= numero >= 10:
    print(f'\ntabuada de{numero}')
for x in range (1,10):
    resultado = numero * x
    print(f'{numero} X {x} = {resultado}')

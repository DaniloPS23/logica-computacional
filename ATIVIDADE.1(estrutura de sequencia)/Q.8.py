8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora= float(input('quanto voce ganha: '))
horas_trabalho= float(input('quantas horas voce trabalha por mês: '))
salário_total= valor_hora*horas_trabalho
print(f"Seu salário total no mês é: R${salário_total:.2f}")

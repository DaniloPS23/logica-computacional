9 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. 
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
1- salários até R$ 280,00 (incluindo) : aumento de 20%
2- salários entre R 280,00eR  700,00 : aumento de 15%
3- salários entre R 700,00eR  1500,00 : aumento de 10%
4- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
. o salário antes do reajuste;
. o percentual de aumento aplicado;
. o valor do aumento;
. o valor do aumento;

salario_atual = float(input("Digite o salário atual do colaborador: "))
if salario_atual <= 280:
    percentual_aumento = 20
elif salario_atual <= 700:
    percentual_aumento = 15
elif salario_atual <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5
aumento = (percentual_aumento / 100) * salario_atual
novo_salario = salario_atual + aumento
print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")

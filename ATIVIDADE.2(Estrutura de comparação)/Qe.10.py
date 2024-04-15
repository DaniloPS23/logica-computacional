10 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, 
caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. Dicas:
. Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
. Triângulo Equilátero: três lados iguais;
. Triângulo Isósceles: quaisquer dois lados iguais;
. Triângulo Escaleno: três lados diferentes;

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        tipo_triangulo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo_triangulo = "Isósceles"
    else:
        tipo_triangulo = "Escaleno"
    print(f"Os lados formam um triângulo {tipo_triangulo}.")
else:
    print("Os lados fornecidos não formam um triângulo.")

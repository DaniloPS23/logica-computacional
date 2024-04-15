7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Digite o lado do quadrado: "))
area = lado ** 2
dobro_area = 2 * area
print(f"A área do quadrado com lado {lado} é: {area}")
print(f"O dobro da área é: {dobro_area}")

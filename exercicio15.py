"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

"""

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))


if (lado1 + lado2 > lado3) and \
   (lado1 + lado3 > lado2) and \
   (lado2 + lado3 > lado1):
    

    print("\nOs lados informados PODEM formar um triângulo.")
    
    if lado1 == lado2 and lado2 == lado3:
        print("É um TRIÂNGULO EQUILÁTERO (todos os lados iguais).")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("É um TRIÂNGULO ISÓSCELES (dois lados iguais).")
    else:
        print("É um TRIÂNGULO ESCALENO (todos os lados diferentes).")
else:
    print("\nOs lados informados NÃO PODEM formar um triângulo.")
    print("A soma de quaisquer dois lados deve ser maior que o terceiro.")
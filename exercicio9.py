"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

numeros = [numero1, numero2, numero3]

numeros_ordenados = sorted(numeros, reverse=True)

print("Os números em ordem decrescente são:")

for numero in numeros_ordenados:
    print(numero)

print(f"Os números em ordem decrescente são: {numeros_ordenados[0]}, {numeros_ordenados[1]} e {numeros_ordenados[2]}")

"""
Faça um Programa que leia três números e mostre o maior e o menor deles.

"""
numero1 = int(input('digite o primeiro numero: '))
numero2 = int(input('digite o segundo numero: '))
numero3 = int(input('digite o terceiro numero: '))

menor = min(numero1, numero2, numero3)
maior = max(numero1, numero2, numero3)

print(f'O maior numero digitado é: {maior}')
print(f'O menor numero digitado é: {menor}')

"""
Faça um Programa que leia três números e mostre o maior deles.
"""

numero1 = int(input('digite o primeiro numero: '))
numero2 = int(input('digite o segundo numero: '))
numero3 = int(input('digite o terceiro numero: '))

if numero1 >= numero2 and numero1 >= numero3:
   maior = numero1
elif numero2 >= numero1 and numero2 >= numero3:
   maior = numero2
else: 
   maior = numero3

print(f'o maior numero digitado é: {maior}')


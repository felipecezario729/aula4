"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

"""

numero_dia = int(input("Digite um número de 1 a 7 para ver o dia da semana (1-Domingo, 2-Segunda, etc.): "))

if numero_dia == 1:
    print("1 - Domingo")
elif numero_dia == 2:
    print("2 - Segunda-feira")
elif numero_dia == 3:
    print("3 - Terça-feira")
elif numero_dia == 4:
    print("4 - Quarta-feira")
elif numero_dia == 5:
    print("5 - Quinta-feira")
elif numero_dia == 6:
    print("6 - Sexta-feira")
elif numero_dia == 7:
    print("7 - Sábado")
else:
    print("Valor Inválido! Por favor, digite um número entre 1 e 7.")
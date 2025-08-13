"""
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

"""

ano  = int(input('digite um numero'))

if (ano % 4 == 0 and ano != 0) or (ano % 400 == 0):
    print(f'{ano} é ano bissexto')
else: 
    print(f'{ano} não é um  ano bissexto')
    

           
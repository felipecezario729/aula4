"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
"""
try:
    nota1 = int(input('digite uma nota'))
    nota2 = int(input('digite nota2'))
    media = (nota1 + nota2) / 2
    if media == 10:
            print('Aprovado com distinção')
    elif media >= 7:
        print('Aprovado') 
    else:
        print("R") 
except:
    print('digite um valor valido')
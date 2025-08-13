"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento

Entre 9.0 e 10.0 : A
Entre 7.5 e 9.0 : B
Entre 6.0 e 7.5 : C
Entre 4.0 e 6.0 : D
Entre 4.0 e zero : E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

# 1. Solicita as duas notas parciais do aluno

nota1 = float(input("Digite a primeira nota parcial: "))
nota2 = float(input("Digite a segunda nota parcial: "))

# 2. Calcula a média das notas
media = (nota1 + nota2) / 2

# 3. Determina o conceito e a situação do aluno
if 9.0 <= media <= 10.0:
    conceito = "A"
    status = "APROVADO"
elif 7.5 <= media < 9.0:
    conceito = "B"
    status = "APROVADO"
elif 6.0 <= media < 7.5:
    conceito = "C"
    status = "APROVADO"
elif 4.0 <= media < 6.0:
    conceito = "D"
    status = "REPROVADO"
else:  # média entre 0 e 4.0
    conceito = "E"
    status = "REPROVADO"

# 4. Exibe os resultados na tela
print(f"\nNotas: Primeira Nota = {nota1:.1f}, Segunda Nota = {nota2:.1f}")
print(f"Média de Aproveitamento: {media:.1f}")
print(f"Conceito: {conceito}")
print(f"Status: {status}")
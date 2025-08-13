"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
 Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
 Caso contrário, ele será classificado como "Inocente".
"""
# Programa de investigação de crime

# Lista de perguntas
perguntas = [
    "Telefonou para a vítima? (sim/não) ",
    "Esteve no local do crime? (sim/não) ",
    "Mora perto da vítima? (sim/não) ",
    "Devia para a vítima? (sim/não) ",
    "Já trabalhou com a vítima? (sim/não) "
]

respostas_positivas = 0

# Fazendo as perguntas
for pergunta in perguntas:
    resposta = input(pergunta).strip().lower()
    if resposta == "sim":
        respostas_positivas += 1

# Classificando a pessoa
if respostas_positivas == 5:
    classificacao = "Assassino"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 2:
    classificacao = "Suspeita"
else:
    classificacao = "Inocente"

# Mostrando o resultado
print(f"\nClassificação: {classificacao}")

"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
# 1. Pergunta o preço de cada um dos três produtos

preco1 = float(input("Digite o preço do primeiro produto: R$ "))
preco2 = float(input("Digite o preço do segundo produto: R$ "))
preco3 = float(input("Digite o preço do terceiro produto: R$ "))


menor_preco = min(preco1, preco2, preco3)

# 3. Informa qual produto tem o menor preço

if menor_preco == preco1:
    print("Você deve comprar o PRIMEIRO produto, pois ele é o mais barato (R$ {:.2f}).".format(menor_preco))
elif menor_preco == preco2:
    print("Você deve comprar o SEGUNDO produto, pois ele é o mais barato (R$ {:.2f}).".format(menor_preco))
else:
    print("Você deve comprar o TERCEIRO produto, pois ele é o mais barato (R$ {:.2f}).".format(menor_preco))
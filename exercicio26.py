"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:

até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:

até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se 
que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

# Preços por litro
preco_alcool = 1.90
preco_gasolina = 2.50

# Entrada de dados
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").strip().upper()
litros = float(input("Digite a quantidade de litros vendidos: "))

# Inicializa o desconto
desconto = 0

# Calculando o desconto conforme tipo e quantidade
if tipo == "A":
    if litros <= 20:
        desconto = 0.03  # 3%
    else:
        desconto = 0.05  # 5%
    preco_litro = preco_alcool
elif tipo == "G":
    if litros <= 20:
        desconto = 0.04  # 4%
    else:
        desconto = 0.06  # 6%
    preco_litro = preco_gasolina
else:
    print("Tipo de combustível inválido!")
    exit()

# Calculando valor a pagar
valor_total = litros * preco_litro
valor_com_desconto = valor_total * (1 - desconto)

# Exibindo o resultado
print(f"\nTipo de combustível: {'Álcool' if tipo == 'A' else 'Gasolina'}")
print(f"Litros vendidos: {litros:.2f} L")
print(f"Preço por litro: R$ {preco_litro:.2f}")
print(f"Desconto aplicado: {desconto*100:.0f}%")
print(f"Valor a pagar: R$ {valor_com_desconto:.2f}")


"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
Confira:

Até 5 Kg:

File Duplo R$ 4,90 por Kg
Alcatra R$ 5,90 por Kg
Picanha R$ 6,90 por Kg
Acima de 5 Kg:

File Duplo R$ 5,80 por Kg
Alcatra R$ 6,80 por Kg
Picanha R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
 porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
 Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
 tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""
# Entrada de dados
print("Tipos de carne disponíveis: File Duplo, Alcatra, Picanha")
tipo = input("Digite o tipo de carne: ").strip().capitalize()
quantidade = float(input("Quantidade em Kg: "))

# Definir preço por Kg
if tipo == "File duplo":
    if quantidade <= 5:
        preco_kg = 4.90
    else:
        preco_kg = 5.80
elif tipo == "Alcatra":
    if quantidade <= 5:
        preco_kg = 5.90
    else:
        preco_kg = 6.80
elif tipo == "Picanha":
    if quantidade <= 5:
        preco_kg = 6.90
    else:
        preco_kg = 7.80
else:
    print("Tipo de carne inválido!")
    preco_kg = 0

# Calcular valor total
total = quantidade * preco_kg

# Tipo de pagamento
pagamento = input("Digite o tipo de pagamento (Dinheiro / Cartão Tabajara): ").strip().lower()
if pagamento == "cartão tabajara" or pagamento == "cartao tabajara":
    desconto = total * 0.05
else:
    desconto = 0.0

valor_final = total - desconto

# Gerar cupom fiscal
print("\n======= CUPOM FISCAL =======")
print(f"Tipo de carne: {tipo}")
print(f"Quantidade: {quantidade:.2f} Kg")
print(f"Preço total: R$ {total:.2f}")
print(f"Tipo de pagamento: {pagamento.capitalize()}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_final:.2f}")
print("============================")

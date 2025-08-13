"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
Até 5 Kg:

Morango R$ 2,50 por Kg
Maçã R$ 1,80 por Kg
Acima de 5 Kg:

Morango R$ 2,20 por Kg

Maçã R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
 receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) 
de maças adquiridas e escreva o valor a ser pago pelo cliente.

"""


# Leitura das quantidades
morango = float(input("Quantos Kg de morango? "))
maca = float(input("Quantos Kg de maçã? "))

# Preço por Kg
if morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

# Valor total por fruta
valor_morango = morango * preco_morango
valor_maca = maca * preco_maca

# Total de Kg e valor total
total_kg = morango + maca
total_valor = valor_morango + valor_maca

# Aplicar desconto se necessário
if total_kg > 8 or total_valor > 25:
    total_valor *= 0.9  # desconto de 10%

# Mostrar valor final
print(f"Valor a pagar: R$ {total_valor:.2f}")

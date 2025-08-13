"""
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
valor_salario = float(input('Digite o valor do salário: '))

# Definindo o percentual aplicado conforme o valor do salário
if valor_salario <= 280:
    percentual_aplicado = 0.20
elif valor_salario <= 700:
    percentual_aplicado = 0.15
elif valor_salario <= 1500:
    percentual_aplicado = 0.10
else:  # acima de 1500
    percentual_aplicado = 0.05

# Cálculo do aumento e novo salário
valor_do_aumento = valor_salario * percentual_aplicado
novo_salario = valor_salario + valor_do_aumento

# Exibindo os resultados
print(f'Salário antes do reajuste: R$ {valor_salario:.2f}')
print(f'Percentual de aumento aplicado: {percentual_aplicado * 100:.0f}%')
print(f'Valor do aumento: R$ {valor_do_aumento:.2f}')
print(f'Novo salário: R$ {novo_salario:.2f}')

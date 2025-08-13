"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
 As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
 O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""
try:
    valor = int(input("Valor do saque (entre 10 e 600):"))
except ValueError:
    print("Entrada invalida: digite um número interio.") 
    raise SystemExit
  
  #    A regra do enunciado: mínimo R$10 e máximo R$600.
if valor< 10 or valor > 600:
    print("Valor fora do intervalo permitido (10 a 600).")
    raise SystemExit
#    seleção de notas do caixa eletronico
notas = [100, 50, 10, 5, 1]

distribuição = {}

restante = valor

for nota in notas:
    qtd, restante =  divmod(restante, nota)
    distribuição[nota] = qtd


assert restante == 0

print(f'\nsaque de R$ {valor}:')
for nota in notas:
    qtd = distribuição[nota]
    if qtd > 0:
        palavra_nota = 'nota' if qtd == 1 else 'notas'
        nome_moeda = 'real' if nota == 1 else "reais"
        print(f'{qtd} {palavra_nota} de {nota} {nome_moeda}')

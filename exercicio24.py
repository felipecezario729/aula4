"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
"""

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input(" Digite o segundo número: "))

print("\nEscolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
opcao = input("Digite o número da operação: ")

if opcao == "1":
    resultado = num1 + num2
    operacao = "soma"
elif opcao == "2":
    resultado = num1 - num2
    operacao = "subtração"
elif opcao == "3":
    resultado = num1 * num2
    operacao = "multiplicação"
elif opcao == "4":
    if num2 != 0:
        resultado = num1 / num2
        operacao = "divisão"
    else:
        print("Erro: divisão por zero não é permitida!")
        exit()
else:
    print("Opção inválida!")
    exit()

par_ou_impar = "par" if resultado % 2 == 0 else "ímpar"
positivo_ou_negativo = "positivo" if resultado > 0 else "negativo" if resultado < 0 else "zero"
inteiro_ou_decimal = "inteiro" if resultado.is_integer() else "decimal"

# 5. Exibindo o resultado
print(f"\nO resultado da {operacao} é {resultado}.")
print(f"Esse número é {par_ou_impar}, {positivo_ou_negativo} e {inteiro_ou_decimal}.")

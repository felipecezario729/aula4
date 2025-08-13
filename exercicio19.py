"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
 Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
"""

num = int(input('Digite um número inteiro menor que 1000:'))
if num < 0 or num >= 1000:
    print("número invalido! DIgite um valor entre 0 e 999")
else:
    centenas = num // 100
    dezenas = (num % 100) // 10
    unidade = num % 10

    partes = []


    if centenas > 0:
        partes.append(f'{centenas} centena' if centenas == 1 else f'{centenas} centena')
        
    if dezenas > 0:
        partes.append(f'{dezenas} dezena' if dezenas == 1 else f'{dezenas} dezena')

    if unidade > 0:
        partes.append(f'{unidade} unidade' if unidade == 1 else f'{unidade} unidades')

    if len(partes) == 1:
         frase = partes[0]
    elif len(partes) == 2:
         frase = ' e ' .join(partes)  
    else:
        frase = ", " .join(partes[:-1]) + " e " + partes[-1]

print(frase)




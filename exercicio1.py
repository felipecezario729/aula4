"""
Faça um Programa que peça dois números e imprima o maior deles.

# estrutura de condição

= atribuição   x = 10
== comparação   10 == 10
>  maior    10 > 5
>=  maior ou igual    10 >= 5 
< menor
<= 
operadores lógicos
 and (e) => só executará se todos as condiçoes forem V
 or (ou ) => Basta que uma das condições sejam verdadeiras

"""
try:
    n1 = int(input('digite o 1 nuemro'))
    n2 = int(input('digite o 2 numero'))
    if n1 > n2:

        print('0 maior é ',n1)
    elif n2 >n1:
        print('o maior é',n2) 
    else: 
        print('são iguais')    

except:
     print(' digite um valor numerico')

"""
Faça um Programa que verifique
 se uma letra digitada é vogal ou consoante.

try:
    letra = input('digite uma letra')
    letra = letra.upper()
    #print(letra)
    if letra == 'A' or letra == 'E' or letra =='I' or letra == 'O' or letra == 'U':
        print('A letra digitada é uma vogal')
    else:
        print('è uma consoante')

except:
    print('digite vogal ou consoante')    
"""
try:
    letra = input('Digite uma letra')
    letra = letra.upper() 
    vogais = ['A', 'E', 'I', 'O', 'U']
    consoante = ['B', 'C','D','F','G','H','J','P','K','L','X','N','M','Z','Q','W','R,','V','Y']
    if letra in vogais:
       print('A letra é uma vogal')
    elif letra in consoante:
        print('A letra é uma consoante')   
    else:
        print('o caracter digitado não é uma letra')   
except:
    print('digite vogal ou consoante!')    
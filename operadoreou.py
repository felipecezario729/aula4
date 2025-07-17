dinheiro =  False
senha = False
if dinheiro == True and senha == True:
    print("Sacar")
elif dinheiro == True and senha == False:
    print("senha Invalida")
elif dinheiro == False and senha == True:
    print("Saldo Insuficiente") 
elif dinheiro == False and senha == False:
    print("dados incorretos")


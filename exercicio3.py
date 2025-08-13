"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
letra = input("Digite uma letra (m para masculino ou f para feminino): ").upper() 

if letra == "M":
   print("M - Masculino")
elif letra == "f":
   print("F - Feminino")
else: 
   print("Sexo invalido")


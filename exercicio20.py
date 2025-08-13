"""
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.

"""
n1 = float(input("nota 1:"))
n2 = float(input("nota 2:"))
n3 = float(input("nota 3:"))

# calcular a media das notas 

media = (n1 + n2 + n3) / 3

media_exibida = round(media, 2)

if round(media, 2) == 10:
    print(f'media: {media_exibida} -> Aprovado com Distinção')
elif media >= 7:
    print(f'media: {media_exibida} -> aprovado')
else:
    print(f'media:{media_exibida} -> Reprovado')
            
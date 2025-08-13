"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""
from datetime import datetime
data_str = input("digiter uma data no formato dd/mm/aaaa:")
try:
    data = datetime.strptime(data_str, "%d/%m/%Y")
    print(f"A Data é valida:  {data.strftime("%d/%m/%Y")}")
except ValueError:
    print("Data Invalida!")
    
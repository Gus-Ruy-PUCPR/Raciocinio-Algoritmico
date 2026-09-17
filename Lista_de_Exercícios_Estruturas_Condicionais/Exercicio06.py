# 06. Inteiro ou decimal
# Faça um programa que peça um número e informe se o valor digitado é inteiro ou decimal.
# Dica: um número é inteiro quando ele é igual à sua própria parte inteira; compare o valor lido com int(valor) ou
# com round(valor).

num = float(input("Digite um numero: "))

if int(num) == num:
    print(f"{num} é inteiro!!!")
else:
    print(f"{num} é decimal!!!")
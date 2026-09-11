# 01. Maior de dois números
# Faça um programa que peça dois números e imprima o maior deles. Atenção: o programa deve tratar
# explicitamente o caso em que os dois números são iguais.

num1 = int(input("Digite o numero 1: "))
num2 = int(input("Digite o numero 2: "))

if num1 > num2:
    print(f"{num2} é menor.")
elif num1 < num2:
    print(f"{num1} é menor.")
else:
    print(f"{num1} e {num2} são iguais.")
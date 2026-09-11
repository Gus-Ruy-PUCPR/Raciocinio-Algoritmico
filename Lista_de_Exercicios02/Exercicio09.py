# 09. Maior de três números
# Faça um programa que leia três números e mostre o maior deles.

num1 = int(input("Digite o numero 1: "))
num2 = int(input("Digite o numero 2: "))
num3 = int(input("Digite o numero 3: "))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} é maior!!!")
    else:
        print(f"{num3} é maior!!!")
elif num2 > num3:
    print(f"{num2} é maior!!!")
else:
    print(f"{num3} é maior!!!")
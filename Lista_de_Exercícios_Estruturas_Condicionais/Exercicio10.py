# 10. Maior e menor de três números
# Faça um programa que leia três números e mostre o maior e o menor deles.


num1 = int(input("Digite o numero 1: "))
num2 = int(input("Digite o numero 2: "))
num3 = int(input("Digite o numero 3: "))

#maior
if num1 > num2:
    if num1 > num3:
        maior = num1
    else:
        maior = num3
else:
    if num2 > num3:
        maior = num2
    else:
        maior = num3
#menor
if num1 < num2:
    if num1 < num3:
        menor = num1
    else:
        menor = num3
else:
    if num2 < num3:
        menor = num2
    else:
        menor = num3

print(f"O maior número é {maior} e o menor é {menor}!")
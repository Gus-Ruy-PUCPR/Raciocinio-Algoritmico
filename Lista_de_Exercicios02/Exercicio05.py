# 05. Par ou ímpar
# Faça um programa que peça um número inteiro e determine se ele é par ou ímpar.

num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
    print(f"{num} é par!!!")
else:
    print(f"{num} é impar!!!")
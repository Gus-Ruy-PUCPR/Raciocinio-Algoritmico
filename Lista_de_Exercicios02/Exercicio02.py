# 02. Sinal de um número
# Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo. Observe que o zero
# não é positivo nem negativo, e por isso constitui um terceiro caso.

num = int(input("Digite um numero: "))

if num > 0:
    print(f"{num} é positivo!")
elif num < 0:
    print(f"{num} é negativo!")
else:
    print(f"{num} é nulo!")
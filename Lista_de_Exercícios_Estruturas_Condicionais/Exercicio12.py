# 12. Ordem decrescente
# Faça um programa que leia três números e mostre-os em ordem decrescente.
# Observação: sem o uso de listas e de laços, este problema exige a análise das seis ordens possíveis entre três valores.
# Monte a tabela de casos antes de codificar.

num1 = int(input("Digite o numero 1: "))
num2 = int(input("Digite o numero 2: "))
num3 = int(input("Digite o numero 3: "))

if num1 <= num2 <= num3:
    print(f"{num1}, {num2}. {num3}")
elif num2 <= num1 <= num3:
    print(f"{num2}, {num1}. {num3}")
elif num2 <= num3 <= num1:
    print(f"{num2}, {num3}. {num1}")
elif num3 <= num2 <= num1:
    print(f"{num3}, {num2}. {num1}")
elif num1 <= num3 <= num2:
    print(f"{num1}, {num3}. {num2}")
else:
    print(f"{num3}, {num1}. {num2}")

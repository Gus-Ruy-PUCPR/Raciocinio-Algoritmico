# 22. Equação do segundo grau
# Faça um programa que calcule as raízes de uma equação do segundo grau da forma a*x**2 + b*x + c = 0.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes
# situações:
# • se o valor de a for igual a zero, a equação não é do segundo grau e o programa deve informar o usuário
# e encerrar sem pedir os demais valores;
# • se o delta calculado for negativo, a equação não possui raízes reais — informe ao usuário e encerre;
# • se o delta calculado for igual a zero, a equação possui apenas uma raiz real — informe-a ao usuário;
# • se o delta for positivo, a equação possui duas raízes reais — informe-as ao usuário.
# Lembre-se de que a raiz quadrada deve ser obtida com delta ** 0.5.

a = int(input("Digite o valor de a: "))

if a == 0:
    print("O coeficiente 'a' não pode ser zero. A equação não é do segundo grau.")
else:
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    
    delta = (b ** 2) - (4 * a * c)
    
    if delta < 0:
        print(f"Delta = {delta}. A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"Delta = 0. A equação possui apenas uma raiz real: {raiz:.2f}")
    else:
        raiz1 = (-b + (delta ** 0.5)) / (2 * a)
        raiz2 = (-b - (delta ** 0.5)) / (2 * a)
        print(f"Delta = {delta}. A equação possui duas raízes reais:")
        print(f"Raiz 1: {raiz1:.2f}")
        print(f"Raiz 2: {raiz2:.2f}")
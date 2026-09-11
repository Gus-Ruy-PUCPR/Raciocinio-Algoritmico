# 26. Caixa eletrônico
# Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque e
# depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis são as de 1, 5, 10, 50 e
# 100 reais. O valor mínimo do saque é de 10 reais e o máximo é de 600 reais, sendo o valor sempre inteiro. O
# programa não deve se preocupar com a quantidade de notas existentes na máquina, e deve informar apenas
# as notas efetivamente entregues.
# • Exemplo 1: para sacar 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de
# 5 e uma nota de 1.
# • Exemplo 2: para sacar 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas
# de 10, uma nota de 5 e quatro notas de 1.

saque = int(input("Digite o valor do saque (entre 10 e 600 reais): "))

if saque < 10 or saque > 600:
    print("Erro: O valor do saque deve estar estritamente entre 10 e 600 reais.")
else:
    n100 = saque // 100
    resto = saque % 100

    n50 = resto // 50
    resto = resto % 50

    n10 = resto // 10
    resto = resto % 10

    n5 = resto // 5
    n1 = resto % 5

    print(f"\nPara o saque de R$ {saque}, serão fornecidas:")

    if n100 > 0:
        if n100 == 1:
            print("- 1 nota de R$ 100")
        else:
            print(f"- {n100} notas de R$ 100")

    if n50 > 0:
        if n50 == 1:
            print("- 1 nota de R$ 50")
        else:
            print(f"- {n50} notas de R$ 50")

    if n10 > 0:
        if n10 == 1:
            print("- 1 nota de R$ 10")
        else:
            print(f"- {n10} notas de R$ 10")

    if n5 > 0:
        if n5 == 1:
            print("- 1 nota de R$ 5")
        else:
            print(f"- {n5} notas de R$ 5")

    if n1 > 0:
        if n1 == 1:
            print("- 1 nota de R$ 1")
        else:
            print(f"- {n1} notas de R$ 1")
# 08. Ano bissexto
# Faça um programa que peça um número correspondente a um determinado ano e informe se este ano é ou
# não bissexto.
# Regra: um ano é bissexto quando é divisível por 4 e não é divisível por 100; excepcionalmente, também é bissexto
# quando é divisível por 400.

ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f"{ano} é bissexto!")
else:
    print(f"{ano} não é bissexto!")
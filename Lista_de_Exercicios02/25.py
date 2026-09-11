# 25. Centenas, dezenas e unidades
# Faça um programa que leia um número inteiro entre 0 e 999 e imprima a quantidade de centenas, dezenas
# e unidades do mesmo, observando o plural dos termos, a colocação do "e" e da vírgula. Por exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades
# 100 = 1 centena
# Teste obrigatoriamente com os valores: 326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11,
# 1, 7, 16 e 0.

numero = int(input("Digite um número inteiro entre 0 e 999: "))
if numero < 0 or numero > 999:
    print("Erro: O número deve estar estritamente entre 0 e 999.")
else:
    c = numero // 100
    d = (numero % 100) // 10
    u = numero % 10

    qtd_partes = 0
    if c > 0:
        qtd_partes = qtd_partes + 1
    if d > 0:
        qtd_partes = qtd_partes + 1
    if u > 0:
        qtd_partes = qtd_partes + 1

    print(f"{numero} = ", end="")

    if numero == 0:
        print("0")
    else:
        impressos = 0

        if c > 0:
            if c == 1:
                print("1 centena", end="")
            else:
                print(f"{c} centenas", end="")
            impressos = impressos + 1

        if d > 0:
            if impressos > 0:
                if impressos == qtd_partes - 1:
                    print(" e ", end="")
                else:
                    print(", ", end="")
            
            if d == 1:
                print("1 dezena", end="")
            else:
                print(f"{d} dezenas", end="")
            impressos = impressos + 1

        if u > 0:
            if impressos > 0:
                if impressos == qtd_partes - 1:
                    print(" e ", end="")
                else:
                    print(", ", end="")
            
            if u == 1:
                print("1 unidade", end="")
            else:
                print(f"{u} unidades", end="")

        print()
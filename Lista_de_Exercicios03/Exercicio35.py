# Exercício 35 — Primos gêmeos. Sarah Gabrielli Rodrigues de Souza Ribeiro - 31/08/2026.
# Ler um valor N e mostrar os pares de primos gêmeos entre 2 e N, informar quantos pares foram encontrados.
# Dois primos são gêmeos quando a diferença entre eles é 2.
# Exercício 35 — Primos gêmeos

try:
    N = int(input("Por gentileza, informe um valor máximo: "))
    if N == 2: # SELEÇÃO — só é avaliado se a anterior for falsa
        print('Com o valor "2", nenhum par será encontrado. Por que não tenta outro? ')

    elif N < 2: 
        print("Por favor, diga-me um número maior que 2.")

    else:
        Num = 2
        UltimoPrimo = 0
        QuantidadePares = 0
        Pares = ""

        while True: # REPETIÇÃO CONDICIONAL — quando o número de voltas é desconhecido

            if Num > N: 
                break

            Primo = True # FLAG (variável lógica) — registra que algo aconteceu

            for Divisor in range(2, Num):
                if Num % Divisor == 0:
                    Primo = False
                    break

            if Primo:

                if UltimoPrimo != 0 and Num - UltimoPrimo == 2: 
                    Pares += "(" + str(UltimoPrimo) + ", " + str(Num) + ")\n"
                    QuantidadePares += 1

                UltimoPrimo = Num

            Num += 1 # CONTADOR — conta ocorrência

        print()
        print("Esta é a quantidade de pares de primos gêmeos encontrados:")

        if QuantidadePares == 0: # SELEÇÃO — só é avaliado se a anterior for falsa
            print("Sinto muito, nenhum par foi encontrado.")
        else:
            print(Pares)

        print("Quantidade de pares encontrados:", QuantidadePares)

except ValueError: # EXCEÇÃO — recusa valores fora dos parâmetro
    print("Valor inválido! Tente novamente.")
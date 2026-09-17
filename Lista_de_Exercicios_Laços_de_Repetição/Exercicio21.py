# Exercício 21 — Teste de primalidade. Sarah Gabrielli Rodrigues de Souza Ribeiro - 30/08/2026.
# Pedir um número inteiro positivo e dizer se é ou não um número primo. Divisível por um e ele mesmo.

while True: # REPETIÇÃO CONDICIONAL — quando o número de voltas é desconhecido
    try:
        Num = int(input("Por gentileza, digite um número: "))
        if Num <= 1: 
            print("Número inválido! Digite outro número:")
            continue

        Primo = True # FLAG (variável lógica) — registra que algo aconteceu

        if Num == 1:
            Primo = False

        else:
            for i in range(2, Num): # CONTADOR — conta ocorrência
                if Num % i == 0: 
                    Primo = False # FLAG (variável lógica) — registra que algo aconteceu
                    break

        if Primo:
            print("O número", Num, "se trata de um primo.")
        else:
            print("O número", Num, "não se trata de um primo.")

        break

    except ValueError: # EXCEÇÃO — recusa valores fora dos parâmetro
        print("Valor inválido! Digite um número inteiro:")
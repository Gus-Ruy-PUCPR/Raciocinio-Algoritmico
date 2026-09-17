# Exercício 20 — Fatorial em série. Sarah Gabrielli Rodrigues de Souza Ribeiro - 30/08/2026.
# Fatorial infinito, faixa de num inteiros positivos menores que 16.
# Perguntar se quer continuar

while True:  # REPETIÇÃO CONDICIONAL — quando o número de voltas é desconhecido
    try:
        Num = int(input("Por gentileza, diga o número para calcular o fatorial: "))

        if Num > 16 or Num < 1:  # VALIDAÇÃO (ler-validar-reler) — garante um dado consistente
            print("Número inválido, por gentileza digite um que esteja entre 1 e 16, e seja inteiro.")
            continue # EXCEÇÃO — recusa valores fora dos parâmetros

        Fatorial = 1
        Expressao = "Expressão: "

        for i in range(Num, 0, -1):
            Fatorial *= i
            Expressao += str(i) # CONTADOR — conta as ocorrências

            if i > 1: 
                Expressao += " * " # CONTADOR — conta as ocorrências

        print("O valor fatorial de", Num, "é", Fatorial, Expressao)
        # SENTINELA — encerra leitura de quantidade desconhecida 
        print("Gostaria de prosseguir?")
        Calculos = input('"Sim" para realizar outros cálculos fatoriais e "Não" para encerrar: ')

        if Calculos == "Não" or Calculos == "não":
            break

    except ValueError: # EXCEÇÃO — recusa valores fora dos parâmetros
        print("Valor inválido!")
        continue
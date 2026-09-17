# Exercício 33 — Estatística de temperaturas. Sarah Gabrielli Rodrigues de Souza Ribeiro - 30/08/2026.
# Ler um conjunto indeterminado de temperaturas e informar a menor, a maior e a média das temperaturas.
# -999 para encerrar. Tratar o caso em que nenhuma temperatura é informada (não é permitido dividir por zero).


Soma = 0
Quantidade = 0
Maior = 0
Menor = 0

while True: # REPETIÇÃO CONDICIONAL — quando o número de voltas é desconhecido
    try: # SENTINELA — encerra leitura de quantidade desconhecida
        Temperatura = float(input('Por gentileza, informe uma temperatura ("-999" para encerrar): '))

        if Temperatura == -999:
            break

        if Quantidade == 0:
            Maior = Temperatura
            Menor = Temperatura

        else: # SELEÇÃO — só é avaliado se a anterior for falsa
            if Temperatura > Maior: # MÁXIMO / MÍNIMO — o primeiro valor inicializa a comparação
                Maior = Temperatura

            if Temperatura < Menor:
                Menor = Temperatura

        Soma += Temperatura # ACUMULADOR — soma valores
        Quantidade += 1 # CONTADOR — conta ocorrências

    except ValueError: # EXCEÇÃO — recusa valores fora dos parâmetro
        print("Valor inválido! Digite uma temperatura.")
        continue

if Quantidade == 0:
    print("Não há temperatura alguma aqui, tente novamente.")

else:
    Media = Soma / Quantidade # MÉDIA — pega a soma dos valores e divide pela quantidade

    print("Esta é a maior temperatura:", Maior)
    print("Esta é a menor temperatura:", Menor)
    print("E esta é a média das temperaturas:", Media)

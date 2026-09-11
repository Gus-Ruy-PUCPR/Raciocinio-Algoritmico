# Exercício 18 — Menor, maior e soma. Sarah Gabrielli Rodrigues de Souza Ribeiro - 30/08/2026.
# Com uma quantidade de números ainda desconhecida de números diga o menor, maior e a soma.
Num = -1
Soma = 0
Maior = 0
Menor = 0
NumOrdinal = 1

while True: # REPETIÇÃO CONDICIONAL — quando o número de voltas é desconhecido

    Num = int(input('Por gentileza, diga o ' + str(NumOrdinal) + 'º número ("0" para cessar): '))
    # SENTINELA — encerra leitura de quantidade desconhecida
    if Num == 0:
        break

    Soma += Num # ACUMULADOR — soma os valores

    if NumOrdinal == 1: # SELEÇÃO — só é avaliado se a anterior for falsa
        Maior = Num
        Menor = Num

    else: # VALIDAÇÃO (ler-validar-reler) — garante um dado consistente
        if Num > Maior:
            Maior = Num

        if Num < Menor:
            Menor = Num
    NumOrdinal += 1 # CONTADOR — conta as ocorrências

print("O maior número é:", Maior)
print("O menor número é:", Menor)
print("E a soma deles é:", Soma)
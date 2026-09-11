# Exercício 19 — Menor, maior e soma com faixa. Sarah Gabrielli Rodrigues de Souza Ribeiro - 30/08/2026.
# Pegar o Exercício 18, mas agora com números entre 0 e 1000. 
# Valores além devem ser recusados, sem consumir uma das N leituras.
Num = -1
Soma = 0
Maior = 0
Menor = 0
NumOrdinal = 1

while True: # REPETIÇÃO CONDICIONAL — quando o número de voltas é desconhecido
    try:
        Num = int(input('Por gentileza, diga o ' + str(NumOrdinal) + 'º número ("0" para cessar): '))
    # SENTINELA — encerra leitura de quantidade desconhecida 
        if Num == 0:
            break
        if Num > 1000 or Num < 0: # VALIDAÇÃO (ler-validar-reler) — garante um dado consistente
            print("Número inválido, por gentileza digite um que esteja entre 0 a 1000.")
            continue

    except ValueError: # EXCEÇÃO — recusa valores fora dos parâmetros
        print("Valor inválido!")
        continue

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
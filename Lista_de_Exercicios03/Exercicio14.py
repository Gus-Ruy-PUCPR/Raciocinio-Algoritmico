# Exercício 14 — Pares e ímpares. Sarah Gabrielli Rodrigues de Souza Ribeiro - 26/08/2026.
# Pedir 10 números, contar quantos são pares e quantos são ímpares. Informar ao fim.
Pares = 0
Ímpares = 0
for i in range (10): # REPETIÇÃO CONTADA: quando o número de voltas é conhecido
    num = int(input("Por gentileza, digite o número: ")) 
# Pode ser: print("Digite o n°:") num = int(input())
    if (num %2 == 0): # CONTADOR — conta as ocorrências
        Pares += 1
    else: # SELEÇÃO — só é avaliado se a anterior for falsa
        Ímpares +=1
print("Números pares", Pares, "Números ímpares", Ímpares)
# Exercício 09 — Ímpares até 50. Sarah Gabrielli Rodrigues de Souza Ribeiro - 29/08/2026.
# Exibir apenas os números ímpares entre 1 e 50.
Pares = 0
Impares = 0
print("Estes são os números ímpares entre 1 e 50:")
for i in range (1, 51): # REPETIÇÃO CONTADA: quando o número de voltas é conhecido
    if not (i %2 == 0): # CONTADOR — conta as ocorrências
        Impares += 1
        print(i)

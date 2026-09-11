# Exercício 08 — Soma e média de cinco números. Sarah Gabrielli Rodrigues de Souza Ribeiro - 29/08/2026.
# Pedir cinco números e exibir a soma e a média deles.
Soma = 0
Media = 0
for i in range (5): # REPETIÇÃO CONTADA: quando o número de voltas é conhecido
    Num = int(input("Por gentileza, digite o " + str(i + 1) + " º número: ")) 
    Soma += Num # ACUMULADOR — soma os valores
    Media = Soma / 5 # MÉDIA — pega a soma dos valores e divide pela quantidade
print("A soma destes números é", Soma, "E a sua média é", Media)

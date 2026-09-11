# Exercício 5 — Soma e produto dos elementos
# Nível ●○○○
# Elabore um programa que leia uma lista com 5 números inteiros e mostre os valores lidos, a soma e o produto
# de todos eles.
# Atenção ao valor inicial de cada acumulador.

lista = [1, 2, 3, 4, 5]
soma = 0
produto = 1

# Laço para percorrer a lista e calcular a soma e o produto dos elementos
for i in range(5):
    try:
        soma += lista[i]
        produto *= lista[i]
    except:
        print("Erro ao somar ou multiplicar os elementos da lista.")

print(f"Valores lidos: {lista}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")

#Exercicio 05 - FIM
# Exercício 09 - Thiago Augusto da Silva - 01/09
# Elabore um programa que leia uma lista com 10 números inteiros e, em seguida, um valor a ser procurado.
# O programa deve informar se o valor existe na lista, quantas vezes ocorre e quais posições ocupa. Deve ainda
# apresentar o maior e o menor valor da lista, acompanhados de suas posições.
# Não utilize in, count, index, max ou min ! : o objetivo é construir a varredura manualmente.

import random

valores = []
numEncontrado = int(0)
numPosicao = str()

# Criando a lista de valores
for i in range(10):
    num = random.randint(1, 100)  # Substituindo input por geração aleatória para fins de teste
    print("Número digitado:", num)  # Exibe o número gerado
    valores.append(num)

numDesejado = int(input("\nDigite o número que deseja encontrar: "))

if numDesejado not in valores:
    print("Este número não foi encontrado na lista!")

else:
    for i in range(10):
        if valores[i] == numDesejado:
            numEncontrado += 1
            numPosicao += "Posição "+str(i)+" "
        else: continue
        if i == 9: print(f"\nO número escolhido aparece {numEncontrado} vezes\nE foi encontrado nas posições: {numPosicao}") 
# A última linha foi inserida dentro do for para evitar o caso do número não ser encontrado e ainda sim imprimir "Numero escolhido aparece 0 vezes(...)"

# Exercício 09 - Fim

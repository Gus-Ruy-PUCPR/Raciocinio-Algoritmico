# Exercício 09 - Thiago Augusto da Silva - 01/09
# Elabore um programa que leia uma lista com 10 números inteiros e, em seguida, um valor a ser procurado.
# O programa deve informar se o valor existe na lista, quantas vezes ocorre e quais posições ocupa. Deve ainda
# apresentar o maior e o menor valor da lista, acompanhados de suas posições.
# Não utilize in, count, index, max ou min ! : o objetivo é construir a varredura manualmente.

valores = []
numEncontrado = int(0)
numPosicao = str()

# Criando a lista de valores
for i in range(10):
    num = int(input(f"Digite o {i+1}o número inteiro: "))
    valores.append(num)

numDesejado = int(input("\nDigite o número que deseja encontrar: "))

if numDesejado not in valores:
    print("Este número não foi encontrado na lista!")

elif numDesejado in valores:
    for i in range(10):
        if valores[i] == numDesejado:
            numEncontrado += 1
            numPosicao += "Posição "+str(i)+" "
        else: continue
        if i == 9: print(f"\nO número escolhido aparece {numEncontrado} vezes\nE foi encontrado nas posições: {numPosicao}") 
# A última linha foi inserida dentro do for para evitar o caso do número não ser encontrado e ainda sim imprimir "Numero escolhido aparece 0 vezes(...)"
# Exercício 09 - Fim
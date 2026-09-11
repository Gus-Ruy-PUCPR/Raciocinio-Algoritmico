# Exercício 07 — Separação de pares e ímpares
# Nível 2 — Básico · Padrão algorítmico: Classificação de elementos em listas
# Elabore um programa que leia 20 números inteiros e os armazene em uma lista.
# Distribua os valores lidos em outras duas listas: uma com os números pares
# e outra com os números ímpares.
# Ao final, exiba as três listas e a quantidade de elementos de cada uma.

import random

# Cria uma lista vazia para guardar todos os números.
numeros = []
# Cria uma lista vazia para guardar somente os números pares.
pares = []
# Cria uma lista vazia para guardar somente os números ímpares.
impares = []
# Repete o bloco abaixo 20 vezes.
for i in range(20):
    # Pede um número inteiro ao usuário.
    numero = random.randint(1, 100)  # Substituindo input por geração aleatória para fins de teste
    print("Número digitado:", numero)  # Exibe o número gerado
    # Guarda o número na lista completa.
    numeros.append(numero)
    # Verifica se o resto da divisão por 2 é zero.
    if numero % 2 == 0:
        # Se for zero, o número é par e vai para a lista de pares.
        pares.append(numero)
    # Caso o número não seja par, executa o bloco abaixo.
    else:
        # Guarda o número na lista de ímpares.
        impares.append(numero)
# Mostra a lista com todos os números digitados.
print("Lista completa:", numeros)
# len informa quantos números existem na lista completa.
print("Quantidade:", len(numeros))
# Mostra a lista de números pares.
print("Números pares:", pares)
# Mostra a quantidade de números pares.
print("Quantidade:", len(pares))
# Mostra a lista de números ímpares.
print("Números ímpares:", impares)
# Mostra a quantidade de números ímpares.
print("Quantidade:", len(impares))

# Exercício 07 - Fim
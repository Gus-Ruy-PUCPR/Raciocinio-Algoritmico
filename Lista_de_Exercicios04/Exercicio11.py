# Exercício 11 — Intercalação de três listas
# Adriel Guilherme de Paula Oliveira - 09/09/2026
import random
# Criar as três listas
lista_a = []
lista_b = []
lista_c = []

# Ler os 10 elementos da lista A
for i in range(10):
    valor = random.randint(1, 100)  # Substituindo input por geração aleatória para fins de teste
    print("Número digitado para a lista A:", valor)  # Exibe o número
    lista_a.append(valor)

# Ler os 10 elementos da lista B
for i in range(10):
    valor = random.randint(1, 100)  # Substituindo input por geração aleatória para fins de teste
    print("Número digitado para a lista B:", valor)  # Exibe o número
    lista_b.append(valor)

# Ler os 10 elementos da lista C
for i in range(10):
    valor = random.randint(1, 100)  # Substituindo input por geração aleatória para fins de teste
    print("Número digitado para a lista C:", valor)  # Exibe o número
    lista_c.append(valor)

# Criar a lista final
lista_final = []

# Intercalar os elementos das três listas
for i in range(10):
    lista_final.append(lista_a[i])
    lista_final.append(lista_b[i])
    lista_final.append(lista_c[i])

# Exibir as três listas
print("\nLista A:", lista_a)
print("Lista B:", lista_b)
print("Lista C:", lista_c)

# Exibir a lista final
print("Lista final:", lista_final)

#Exercicio 11 - FIM
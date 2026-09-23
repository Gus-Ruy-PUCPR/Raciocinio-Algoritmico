# Exercício 05 — Soma e produto dos elementos
# Nível 1 — Básico · Padrão algorítmico: Acumuladores
import random
numeros = []

# entrada dos 5 números
for i in range(5):
    while 1:
        try:
            numero = random.randint(0,10) #int(input("Digite um número inteiro: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

# inicialização dos acumuladores
soma = 0
produto = 1

# cálculo da soma e do produto
for i in range(5):
    soma = soma + numeros[i]
    produto = produto * numeros[i]

# exibição dos resultados
print("Valores lidos:", numeros)
print("Soma:", soma)
print("Produto:", produto)
# Exercício 06 — Soma dos quadrado
# Nível 1 — Básico · Padrão algorítmico: Percurso de lista e acumulador
import random
numeros = []

# entrada dos 10 números
for i in range(10):
    while 1:
        try:
            numero = random.randint(0,10) #int(input("Digite um número inteiro: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

# inicialização do acumulador
soma = 0

# cálculo da soma dos quadrados
for i in range(10):
    soma = soma + numeros[i] * numeros[i]

# exibição do resultado
print("Lista:", numeros)
print("Soma dos quadrados:", soma)
# Exercício 06 — Soma dos quadrados
# Nível 1 — Aquecimento · Padrão algorítmico: Percurso de lista e acumulador
# Elabore um programa que leia uma lista A com 10 números inteiros e calcule
# e mostre a soma dos quadrados de seus elementos.

# Cria uma lista vazia para guardar os números digitados.
numeros = []
# Começa a soma com o valor zero.
soma = 0
# Repete o bloco abaixo 10 vezes.
for i in range(10):
    # Pede um número inteiro ao usuário e guarda em numero.
    numero = int(input("Digite um número inteiro: "))
    # Adiciona o número digitado à lista.
    numeros.append(numero)
# Percorre novamente as 10 posições da lista.
for i in range(10):
    # Multiplica o número por ele mesmo e acrescenta o resultado à soma.
    soma = soma + numeros[i] * numeros[i]
# Mostra a soma dos quadrados de todos os números.
print("Soma dos quadrados:", soma)

# Exercício 06 - Fim
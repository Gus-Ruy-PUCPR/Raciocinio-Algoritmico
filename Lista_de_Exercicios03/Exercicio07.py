# Exercício 07 — Maior de cinco números
# Nível 2 — Fundamental · Padrão algorítmico: Máximo
# Faça um programa que leia 5 números e informe o maior deles.
# Dica: Não inicialize a variável maior com zero: se todos os números forem negativos, o resultado ficaria errado. Use a primeira
# leitura para inicializar.

# Lê o primeiro número e inicializa a variável maior
maior = int(input("Digite o 1º número: "))

# Repete para os 4 números restantes
for i in range(2, 6):
    numero = int(input(f"Digite o {i} número: "))
    if numero > maior:
        maior = numero

print(f"O maior número digitado foi: {maior}")
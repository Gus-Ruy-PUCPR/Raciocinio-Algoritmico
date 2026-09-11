# Exercício 11 — Intervalo com soma
# Nível 2 — Fundamental · Padrão algorítmico: Laço contado + acumulador
# Altere o programa do exercício 10 para mostrar, ao final, a soma de todos os números gerados.

# Leitura de dois números
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

# Define inicio e fim
if a < b:
    inicio = a
    fim = b
else:
    inicio = b
    fim = a

# Acumulador para guardar a soma
soma = 0

print(f"Números no intervalo entre {inicio} e {fim}:")

# Gera o intervalo e acumula os valores
for numero in range(inicio, fim + 1):
    print(numero, end=" ")
    soma += numero

print(f"\nSoma dos números do intervalo: {soma}")
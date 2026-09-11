# Exercício 24 - Lista de Exercícios 03
# Leitura e validação da quantidade de notas N (deve ser > 0)
n = int(input("Informe a quantidade de notas (N > 0): "))
while n <= 0:
    print("Erro: A quantidade de notas deve ser maior que zero.")
    n = int(input("Informe a quantidade de notas (N > 0): "))

soma = 0.0

# Leitura e acumulação das N notas
for i in range(1, n + 1):
    nota = float(input(f"Digite a {i}ª nota (0 a 10): "))
    
    # Validação da nota individual
    while nota < 0 or nota > 10:
        print("Erro: Nota inválida! A nota deve estar entre 0 e 10.")
        nota = float(input(f"Digite a {i}ª nota (0 a 10): "))
    
    soma += nota

# Cálculo da média aritmética
media = soma / n

print(f"\nSoma total das notas: {soma:.2f}")
print(f"Média das {n} notas: {media:.2f}")
# Exercício 25 - Lista de Exercícios 03
# Leitura e validação da quantidade de pessoas N (deve ser > 0)
n = int(input("Informe a quantidade de pessoas na turma (N > 0): "))
while n <= 0:
    print("Erro: A quantidade de pessoas deve ser maior que zero.")
    n = int(input("Informe a quantidade de pessoas na turma (N > 0): "))

soma_idades = 0

# Leitura e acúmulo das idades
for i in range(1, n + 1):
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    
    # Validação da idade individual
    while idade < 0:
        print("Erro: A idade não pode ser negativa.")
        idade = int(input(f"Digite a idade da {i}ª pessoa: "))
        
    soma_idades += idade

# Cálculo da média de idade
media = soma_idades / n

# Classificação da turma com base na média
if media <= 25:
    classificacao = "JOVEM"
elif media <= 60:
    classificacao = "ADULTA"
else:
    classificacao = "IDOSA"

print(f"\nMédia de idade da turma: {media:.2f} anos")
print(f"Classificação da turma: {classificacao}")
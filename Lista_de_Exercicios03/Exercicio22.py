# Exercício 22 — Primalidade com divisores
# Nível 3 — Aplicação · Padrão algorítmico: Reprocessamento
# Altere o programa do exercício 21 para que, caso o número não seja primo, sejam exibidos todos os números
# pelos quais ele é divisível.

# Leitura e validação da entrada (deve ser um inteiro > 0)
numero = int(input("Digite um número inteiro positivo: "))
while numero <= 0:
    print("Erro: O número deve ser maior que zero.")
    numero = int(input("Digite um número inteiro positivo: "))

# Estruturas para acompanhar os divisores
total_divisores = 0
divisores = []

# Procura por todos os divisores de 1 até o próprio número
for i in range(1, numero + 1):
    if numero % i == 0:
        total_divisores += 1
        divisores.append(i)

# Verificação de primalidade (um número é primo se possui EXATAMENTE 2 divisores: 1 e ele mesmo)
if total_divisores == 2:
    print(f"\nO número {numero} É PRIMO!")
else:
    print(f"\nO número {numero} NÃO É PRIMO.")
    print(f"Total de divisores encontrados: {total_divisores}")
    print("Divisores:", ", ".join(map(str, divisores)))
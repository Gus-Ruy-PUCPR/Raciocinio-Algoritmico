# Exercício 34 - Lista de Exercícios 03
# Leitura e validação da entrada (deve ser um inteiro > 0)
n = int(input("Digite um número inteiro positivo: "))
while n <= 0:
    print("Erro: O número deve ser maior que zero.")
    n = int(input("Digite um número inteiro positivo: "))

# Versão (a): Testando todos os divisores de 1 até n
testes_a = 0
divisores_a = 0

for i in range(1, n + 1):
    testes_a += 1
    if n % i == 0:
        divisores_a += 1

primo_a = (divisores_a == 2)


# Versão (b): Testando apenas 2 e ímpares até sqrt(n)
testes_b = 0
primo_b = True

if n == 1:
    primo_b = False
elif n == 2:
    primo_b = True
elif n % 2 == 0:
    testes_b += 1
    primo_b = False
else:
    testes_b += 1  # Conta o teste do par (n % 2)
    divisor = 3
    while divisor * divisor <= n:
        testes_b += 1
        if n % divisor == 0:
            primo_b = False
            break
        divisor += 2

# Exibição e Comparação dos Resultados
print(f" Resultado para N = {n}")
print(f"Versão (a) - Força Bruta  : {'É PRIMO' if primo_a else 'NÃO É PRIMO'}")
print(f"Versão (b) - Otimizada    : {'É PRIMO' if primo_b else 'NÃO É PRIMO'}")

print(f"\nConcordância das versões  : {'SIM' if primo_a == primo_b else 'NÃO'}")
print(f"Testes na versão (a) (1 até n)  : {testes_a}")
print(f"Testes na versão (b) (até √n)   : {testes_b}")
# Exercício 23 — Primos até N e custo do algoritmo
# Nível 4 — Desafio · Padrão algorítmico: Laços aninhados + análise de eficiência
# Faça um programa que mostre todos os primos entre 1 e N, sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões (testes de resto) que executou para encontrar os
# primos.
# Serão avaliados o funcionamento, o estilo e o número de testes executados — quanto menos divisões, melhor.
# Dica: Duas otimizações valem muito: descartar os pares maiores que 2 e parar de testar divisores quando i * i ultrapassar o
# número.

# Leitura e validação da entrada
n = int(input("Informe o valor de N (N >= 2): "))
while n < 2:
    print("Erro: N deve ser maior ou igual a 2.")
    n = int(input("Informe o valor de N (N >= 2): "))

total_divisoes = 0

print(f"\nNúmeros primos entre 1 e {n}:")

# O número 2 é o único primo par
if n >= 2:
    print(2, end=" ")

# Testa apenas os números ímpares de 3 até N
for candidato in range(3, n + 1, 2):
    eh_primo = True
    divisor = 3

    # Testa divisores ímpares enquanto divisor * divisor <= candidato
    while divisor * divisor <= candidato:
        total_divisoes += 1
        if candidato % divisor == 0:
            eh_primo = False
            break  # Interrompe ao achar o primeiro divisor
        divisor += 2

    if eh_primo:
        print(candidato, end=" ")

print(f"\nTotal de testes de resto (%) executados: {total_divisoes}")
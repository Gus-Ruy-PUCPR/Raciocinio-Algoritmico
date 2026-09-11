# Exercício 16 — Fibonacci até ultrapassar 500
# Nível 3 — Aplicação · Padrão algorítmico: Geração de série + parada por valor
# Faça um programa que gere a série de Fibonacci (mesma convenção do exercício 15) exibindo todos os termos
# menores ou iguais a 500. Ao final, informe qual foi o primeiro termo que ultrapassou esse limite.
# Compare com o exercício 15: lá a parada depende de um contador; aqui, do valor produzido.

# Inicialização dos dois primeiros termos (F1 = 1 e F2 = 1)
a, b = 1, 1

print("Série de Fibonacci até 500:")

# Exibe os dois primeiros termos
print(a, end=" ")
print(b, end=" ")

# O próximo termo inicial para a verificação
proximo = a + b

# Continua enquanto o próximo termo for menor ou igual a 500
while proximo <= 500:
    print(proximo, end=" ")
    a, b = b, proximo
    proximo = a + b

print()  # Quebra de linha
print(f"\nO primeiro termo que ultrapassou 500 foi: {proximo}")
# Exercício 04 — Corrida populacional
# Nível 3 — Aplicação · Padrão algorítmico: Laço de convergência (while)
# A população do país A é de 80.000 habitantes, com taxa anual de crescimento de 3%. A população do país B é de
# 200.000 habitantes, com taxa de 1,5% ao ano. Faça um programa que calcule e escreva o número de anos
# necessários para que a população de A ultrapasse ou iguale a de B, mantidas as taxas.
# Exiba também as duas populações no ano em que isso ocorre.
# Dica: O número de repetições é desconhecido de antemão: esse é o caso típico do while. Cada volta do laço representa um ano.

# População inicial
populacao_a = 80000
populacao_b = 200000

# Taxas anuais de crescimento
taxa_a = 0.03   # 3%
taxa_b = 0.015  # 1.5%

# Contador de anos
anos = 0

# O laço executa enquanto a população de A for menor que a de B
while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_a
    populacao_b += populacao_b * taxa_b
    anos += 1

print(f"Quantidade de anos necessários: {anos}")
print(f"População do País A: {int(populacao_a):,} habitantes".replace(",", "."))
print(f"População do País B: {int(populacao_b):,} habitantes".replace(",", "."))
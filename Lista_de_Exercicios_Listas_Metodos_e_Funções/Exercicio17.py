# Exercício 17 — Faixas salariais de vendedores
# Adriel Guilherme de Paula Oliveira - 09/09/2026

# Lista de contadores das faixas salariais
contadores = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Contador de vendedores
vendedores = 0

# Ler o valor das vendas
vendas = float(input("Digite o valor das vendas brutas do vendedor: "))

while vendas >= 0:

    # Calcular o salário do vendedor
    salario = 2000 + (vendas * 0.09)

    # Calcular a posição da lista diretamente pelo salário
    posicao = int((salario - 2000) // 1000)

    # Salários a partir de R$ 10.000,00 ficam na última posição
    if posicao > 7:
        posicao = 8

    # Contabilizar o vendedor na faixa correspondente
    contadores[posicao] = contadores[posicao] + 1

    vendedores = vendedores + 1

    # Ler o próximo vendedor
    vendas = float(input("Digite o valor das vendas brutas do vendedor: "))

# Exibir o relatório
print("\nVendedores processados:", vendedores)

print("\nFaixa salarial                 Vendedores")
print("------------------------------------------")
print("R$ 2.000,00 a R$ 2.999,99          ", contadores[0])
print("R$ 3.000,00 a R$ 3.999,99          ", contadores[1])
print("R$ 4.000,00 a R$ 4.999,99          ", contadores[2])
print("R$ 5.000,00 a R$ 5.999,99          ", contadores[3])
print("R$ 6.000,00 a R$ 6.999,99          ", contadores[4])
print("R$ 7.000,00 a R$ 7.999,99          ", contadores[5])
print("R$ 8.000,00 a R$ 8.999,99          ", contadores[6])
print("R$ 9.000,00 a R$ 9.999,99          ", contadores[7])
print("R$ 10.000,00 ou mais               ", contadores[8])

#Exercicio 17 – FIM

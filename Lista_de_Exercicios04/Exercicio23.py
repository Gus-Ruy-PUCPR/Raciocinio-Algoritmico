# Exercício 23 — Triagem de periféricos para descarte
# Adriel Guilherme de Paula Oliveira - 09/09/2026

# Lista de contadores para as quatro situações
contadores = [0, 0, 0, 0]

# Quantidade total de equipamentos inspecionados
quantidade_total = 0

# Ler a identificação do equipamento
identificacao = int(input("Digite a identificação do equipamento: "))

while identificacao != 0:

    # Ler a situação do equipamento
    situacao = int(input("Digite o código da situação (1 a 4): "))

    # Rejeitar códigos de situação inválidos
    while situacao < 1 or situacao > 4:
        print("Código de situação inválido.")
        situacao = int(input("Digite o código da situação (1 a 4): "))

    # A posição da lista é o código menos 1
    posicao = situacao - 1

    # Incrementar o contador da situação
    contadores[posicao] = contadores[posicao] + 1

    # Incrementar a quantidade total de equipamentos
    quantidade_total = quantidade_total + 1

    # Ler a identificação do próximo equipamento
    identificacao = int(input("Digite a identificação do equipamento: "))

# Exibir a quantidade total de equipamentos
print("\nQuantidade de equipamentos:", quantidade_total)

# Exibir o relatório das situações
print("\nSituação                                      Qtde    Percentual")
print("----------------------------------------------------------------")

if quantidade_total > 0:
    percentual = (contadores[0] * 100) / quantidade_total
    print("1 - necessita apenas de limpeza              ", contadores[0], "   {:.1f}%".format(percentual))

    percentual = (contadores[1] * 100) / quantidade_total
    print("2 - necessita de troca de cabo ou conector   ", contadores[1], "   {:.1f}%".format(percentual))

    percentual = (contadores[2] * 100) / quantidade_total
    print("3 - bateria ou componente interno defeituoso ", contadores[2], "   {:.1f}%".format(percentual))

    percentual = (contadores[3] * 100) / quantidade_total
    print("4 - inservível, destinado à logística reversa", contadores[3], "   {:.1f}%".format(percentual))
else:
    print("Nenhum equipamento foi inspecionado.")

#Exercicio 23 – FIM

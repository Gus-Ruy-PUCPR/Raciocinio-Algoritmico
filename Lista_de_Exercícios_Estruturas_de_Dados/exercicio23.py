# Exercício 23 — Triagem de periféricos para descarte
# Nível 4 — Avançado · Padrão algorítmico: Entrada indeterminada e contadores

contadores = [0, 0, 0, 0, 0]
total = 0

while 1:
    # entrada da identificação do equipamento
    while 1:
        try:
            identificacao = int(input("Digite a identificação (0 para encerrar): "))
            break
        except ValueError:
            print("Entrada inválida! Digite um número.")

    # verifica se deve encerrar
    if identificacao == 0:
        break

    # entrada da situação do equipamento
    while 1:
        try:
            situacao = int(input("Digite a situação (1 a 4): "))

            # validação da situação
            if situacao < 1 or situacao > 4:
                print("Situação inválida! Digite um código de 1 a 4.")
                continue

            break

        except ValueError:
            print("Entrada inválida! Digite um número.")

    # contagem da situação
    contadores[situacao] = contadores[situacao] + 1

    # contagem total dos equipamentos
    total = total + 1

# exibição do relatório
print()
print("Quantidade de equipamentos:", total)

if total > 0:

    print("Situação - Qtde - Percentual")

    # cálculo dos percentuais
    for i in range(1, 5):
        percentual = contadores[i] * 100 / total

        print(i, "-", contadores[i], "-", percentual, "%")

else:
    print("Nenhum equipamento foi informado.")
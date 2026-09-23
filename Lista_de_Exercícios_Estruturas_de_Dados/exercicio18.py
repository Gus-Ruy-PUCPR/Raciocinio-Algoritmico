# cálculo da média
# Exercício 18 — Salto em distância
# Nível 3 — Intermediário · Padrão algorítmico: Entrada indeterminada e acumulador

while 1:

    # entrada do nome do atleta
    nome = input("Digite o nome do atleta: ")

    # verifica se o usuário deseja encerrar
    if nome == "":
        break

    saltos = []

    # entrada dos cinco saltos
    for i in range(5):
        while 1:
            try:
                salto = float(input("Digite a distância do salto: "))
                saltos.append(salto)
                break
            except ValueError:
                print("Entrada inválida! Digite um número.")

    # inicialização do acumulador
    soma = 0

    # cálculo da soma dos cinco saltos
    for i in range(5):
        soma = soma + saltos[i]
    media = soma / 5

    # exibição dos resultados
    print()
    print("Resultado final:")
    print("Atleta:", nome)
    print("Saltos:", saltos[0], "-", saltos[1], "-", saltos[2], "-", saltos[3], "-", saltos[4])
    print("Média dos saltos:", media, "m")
    print()
# Exercício 37 — Censo da academia. Sarah Gabrielli Rodrigues de Souza Ribeiro - 31/08/2026.
# Perguntar para cada cliente, código, altura m e o seu peso kg. Encerrar quando 0 no campo de código.
# informar códigos e valores do cliente mais alto, mais baixo, maior peso e menor peso, média alturas e pesos.
# Tratar caso em que nenhum cliente é cadastrado

SomaAlturas = 0
SomaPesos = 0
Quantidade = 0

while True: # REPETIÇÃO CONDICIONAL — quando o número de voltas é desconhecido
    try: # SENTINELA — encerra leitura de quantidade desconhecida
        Codigo = int(input('Por gentileza, informe o seu código ("0" para encerrar): '))

        if Codigo == 0:
            break

        Altura = float(input("Por favor, diga-me a sua altura (metros): "))
        Peso = float(input("Por favor, diga-me o seu peso (kg): "))

        if Quantidade == 0:

            MaiorAltura = Altura
            MenorAltura = Altura
            MaiorPeso = Peso
            MenorPeso = Peso

            CodigoMaiorAltura = Codigo
            CodigoMenorAltura = Codigo
            CodigoMaiorPeso = Codigo
            CodigoMenorPeso = Codigo

        else: # SELEÇÃO — só é avaliado se a anterior for falsa

            if Altura > MaiorAltura: # MÁXIMO / MÍNIMO — o primeiro valor inicializa a comparação
                MaiorAltura = Altura
                CodigoMaiorAltura = Codigo

            if Altura < MenorAltura:
                MenorAltura = Altura
                CodigoMenorAltura = Codigo

            if Peso > MaiorPeso:
                MaiorPeso = Peso
                CodigoMaiorPeso = Codigo

            if Peso < MenorPeso:
                MenorPeso = Peso
                CodigoMenorPeso = Codigo

        SomaAlturas += Altura # ACUMULADOR — soma valores
        SomaPesos += Peso # ACUMULADOR — soma valores
        Quantidade += 1 # CONTADOR — conta ocorrência

    except ValueError: # EXCEÇÃO — recusa valores fora dos parâmetro
        print("Valor inválido! Por gentileza, digite novamente. Mas corretamente.")
        continue


if Quantidade == 0:
    print("Perdão, mas menhum cliente foi cadastrado.")

else:
    MediaAlturas = SomaAlturas / Quantidade # MÉDIA — pega a soma dos valores e divide pela quantidade
    MediaPesos = SomaPesos / Quantidade

    print()
    print("Cliente mais alto:")
    print("Código:", CodigoMaiorAltura)
    print("Altura:", MaiorAltura, "m")

    print()
    print("Cliente mais baixo:")
    print("Código:", CodigoMenorAltura)
    print("Altura:", MenorAltura, "m")

    print()
    print("Cliente de maior peso:")
    print("Código:", CodigoMaiorPeso)
    print("Peso:", MaiorPeso, "kg")

    print()
    print("Cliente de menor peso:")
    print("Código:", CodigoMenorPeso)
    print("Peso:", MenorPeso, "kg")

    print()
    print("Média das alturas:", MediaAlturas, "m")
    print("Média dos pesos:", MediaPesos, "kg")
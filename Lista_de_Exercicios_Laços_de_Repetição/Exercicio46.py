# Exercício 46 - Lista de Exercícios 03
nome = input("Digite o nome do atleta ou pressione ENTER para encerrar: ")
while nome != "":
    soma = 0
    for contador in range(5):
        salto = float(input("Digite a distância do salto: "))
        while salto < 0:
            print("Distância inválida!")
            salto = float(input("Digite novamente: "))
        soma = soma + salto
        if contador == 0:
            melhor = salto
            pior = salto
        else:
            if salto > melhor:
                melhor = salto
            if salto < pior:
                pior = salto
    media = (soma - melhor - pior) / 3
    print("Atleta:", nome)
    print("Melhor salto:", round(melhor, 2), "m")
    print("Pior salto:", round(pior, 2), "m")
    print("Média dos demais saltos:", round(media, 2), "m")
    nome = input("Digite outro atleta ou pressione ENTER para encerrar: ")
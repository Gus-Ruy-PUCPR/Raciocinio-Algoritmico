# Exercício 26 - Lista de Exercícios 03

eleitores = int(input("Digite o número de eleitores: "))
while eleitores <= 0:
    print("Quantidade inválida!")
    eleitores = int(input("Digite novamente: "))
candidato1 = 0
candidato2 = 0
candidato3 = 0
for contador in range(eleitores):
    voto = int(input("Digite o voto (1, 2 ou 3): "))
    while voto < 1 or voto > 3:
        print("Voto inválido!")
        voto = int(input("Digite o voto novamente: "))
    if voto == 1:
        candidato1 = candidato1 + 1
    elif voto == 2:
        candidato2 = candidato2 + 1
    else:
        candidato3 = candidato3 + 1
print("Votos do candidato 1:", candidato1)
print("Votos do candidato 2:", candidato2)
print("Votos do candidato 3:", candidato3)
#                           Exercício 47 - Thiago Augusto da Silva - 31/08                                          #
#####################################################################################################################
# Em uma competição de ginástica, cada atleta recebe notas de sete jurados. A melhor e a pior nota são eliminadas   #
# e a nota final é a média das cinco restantes.                                                                     #
# Faça um programa que receba o nome do ginasta e as sete notas (de 0 a 10, não ordenadas) e informe a melhor       #
# nota, a pior nota e a média final. O programa encerra quando o nome não for informado.                            #
#####################################################################################################################

# Criamos estas variaveis agora para evitar erros depois
notasFinais = str("") 
notaMenor = float(0.0)
notaMaior = float(0.0)
notasTotal = float(0.0)

while True:
    nome = str(input("Digite o nome do atleta (Caso queira encerrar o programa, não digite nada e aperte Enter): "))
    if nome in "":
        exit()
    for i in range(0, 7, 1):
        print("Digite a nota do ",i+1,"o jurado: ")
        nota = float(input(""))
        notaAtual = str(nota)
        if nota < notaMenor or notaMenor == 0.0:
            notaMenor = nota
        elif nota > notaMaior:
            notaMaior = nota
        notasTotal += nota
        if i == 6:
            notasFinais += notaAtual
        else:
            notasFinais += notaAtual + " / "
    media = (notasTotal - (notaMaior + notaMenor)) / 5
    print("Atleta: ", nome)
    print("Notas: ", notasFinais)
    print("Melhor Nota: ", notaMaior)
    print("Pior Nota: ", notaMenor)
    print("Média: ", media)

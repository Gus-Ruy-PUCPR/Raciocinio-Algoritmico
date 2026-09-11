#                           Exercício 45 - Thiago Augusto da Silva - 31/08                                          #
#####################################################################################################################
# Desenvolva um programa que corrija uma prova de 10 questões de múltipla escolha (alternativas de A a E). O        #
# programa pergunta ao aluno a resposta de cada questão, compara com o gabarito e calcula o total de acertos e a    #
# nota (1 ponto por acerto). Após cada aluno, pergunte se outro aluno vai utilizar o sistema.                       #
# Ao final, informe: maior e menor número de acertos; total de alunos atendidos; e a média das notas da turma.      #
# Gabarito oficial: 1-A, 2-B, 3-C, 4-D, 5-E, 6-E, 7-D, 8-C, 9-B, 10-A.                                              #
# Extensão opcional (será retomada na unidade de listas): permitir que o professor digite o gabarito antes do uso   #
# pelos alunos.                                                                                                     #
#####################################################################################################################

# Gabarito oficial: 1-A, 2-B, 3-C, 4-D, 5-E, 6-E, 7-D, 8-C, 9-B, 10-A.
gabarito1 = str("Aa")
gabarito2 = str("Bb")
gabarito3 = str("Cc")
gabarito4 = str("Dd")
gabarito5 = str("Ee")
gabarito6 = str("Ee")
gabarito7 = str("Dd")
gabarito8 = str("Cc")
gabarito9 = str("Bb")
gabarito10 = str("Aa")

# Variaveis sobre os alunos
maiorAcertos = int(0)
menorAcertos = int(0)
alunosAtentidos = int(0)
notasTurma = int(0)

# Variavel para controlar o loop
loopisTrue = int(1)

while loopisTrue == 1:
    nome = str(input("Digite seu nome: "))
    nota = int(0)
    for i in range(0, 10, 1):
        print("Escreva a sua resposta à ", i+1, "a pergunta: ")
        resposta = str(input(""))
        if i == 0 and resposta in gabarito1:
            nota += 1
        elif i == 1 and resposta in gabarito2:
            nota += 1
        elif i == 2 and resposta in gabarito3:
            nota += 1
        elif i == 3 and resposta in gabarito4:
            nota += 1
        elif i == 4 and resposta in gabarito5:
            nota += 1
        elif i == 5 and resposta in gabarito6:
            nota += 1
        elif i == 6 and resposta in gabarito7:
            nota += 1
        elif i == 7 and resposta in gabarito8:
            nota += 1
        elif i == 8 and resposta in gabarito9:
            nota += 1
        elif i == 9 and resposta in gabarito10:
            nota += 1
    notasTurma += nota
    if nota < menorAcertos or menorAcertos == 0:
        menorAcertos = nota
    elif nota > maiorAcertos:
        maiorAcertos = nota
    alunosAtentidos += 1
    while True:
        print("Outro aluno ainda usará este sistema? (S/N)")
        resposta = str(input(""))
        if resposta in "Ss":
            break
        elif resposta in "Nn":
            loopisTrue = 0
            break
        else:
            print("Por favor responda sim ou não (S/N)")
            continue

mediaTurma = notasTurma / alunosAtentidos

# Ao final, informe: maior e menor número de acertos; total de alunos atendidos; e a média das notas da turma.      #
print("Maior Acertos | Menor Acertos | Alunos atentidos | Média da turma")
print(maiorAcertos, " | ", menorAcertos, " | ", alunosAtentidos, " | ", mediaTurma)
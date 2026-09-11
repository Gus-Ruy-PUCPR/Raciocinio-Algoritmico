#                            Exercício 39 - Thiago Augusto da Silva - 27/08                                     #
#################################################################################################################
# Faça um programa que leia dez conjuntos de dois valores: o número do aluno e a sua altura em centímetros.     #
# Encontre o aluno mais alto e o mais baixo, mostrando o número de cada um junto com as respectivas alturas.    #
#################################################################################################################

# Variaveis de altura
alturaMenor = int(0)
alturaMaior = int(0)
# variaveis de número
alunoMaior = str("")
alunoMenor = str("")

for i in range(1, 3, 1):
    while True:
        try:
            numAluno = str(input("Insira o nome do aluno: "))
            alturaAluno = float(input("Insira a altura do aluno (em cm): "))
        except:
            print("Tente novamente com valores válidos!")
            continue
        break
    if alturaAluno < alturaMenor or alturaMenor == 0:
        alturaMenor = alturaAluno
        alunoMenor = numAluno
    if alturaAluno > alturaMaior:
        alturaMaior = alturaAluno
        alunoMaior = numAluno
print("O maior aluno foi o aluno ", alunoMaior, " com ", alturaMaior, " cm")
print("O menor aluno foi o aluno ", alunoMenor, " com ", alturaMenor, " cm")
# Exercício 27 - Lista de Exercícios 03

turmas = int(input("Digite a quantidade de turmas: "))
while turmas <= 0:
    print("Quantidade inválida!")
    turmas = int(input("Digite novamente: "))
total_alunos = 0
for contador in range(turmas):
    alunos = int(input("Digite a quantidade de alunos da turma: "))
    while alunos < 1 or alunos > 40:
        print("A turma deve ter entre 1 e 40 alunos!")
        alunos = int(input("Digite novamente: "))
    total_alunos = total_alunos + alunos
media = total_alunos / turmas
print("Média de alunos por turma:", round(media, 2))
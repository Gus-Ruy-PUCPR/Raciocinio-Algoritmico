# Exercício 12 — Médias de uma turma
# Nível ●●○○
# Elabore um programa que leia as quatro notas de 10 alunos, calcule e armazene em uma lista a média de
# cada aluno e, ao final, exiba todas as médias e o número de alunos com média maior ou igual a 7,0.
# Sugestão: use um laço externo para percorrer os alunos e um laço interno para ler as quatro notas de cada
# um.

import random

list_medias = []
notas = []
# Primeiro laço de repetição para percorrer os 10 alunos
for alunos in range(10):
    # Segundo laço de repetição para percorrer as 4 notas de cada aluno
    for i in range(4):
        while True:
            try:
                nota = random.randint(5, 10) # aqui viria o imput, mas para fins de teste, estou usando random.uniform(0, 10)
                if nota < 0 or nota > 10:
                    raise ValueError("Nota inválida. Digite um valor entre 0 e 10.") # levanta erro para notas inválidas
                notas.append(nota)
                break
            except ValueError as e:
                print(e) # exibe a mensagem de erro
    soma = 0
    # Laço para calcular a soma das notas de cada aluno
    for nota in notas:
        soma += nota

    media = soma / len(notas)
    list_medias.append(media)
# Laço do tamanho de list_medias para exibir as médias de cada aluno
for i in range(len(list_medias)):
    print(f"Aluno {i + 1}: {list_medias[i]:.1f}") # Printa todos os alunos e suas medias, com uma casa decimal

print("--" * 20)
# Laço para percorrer a lista de médias e exibir os alunos com média maior ou igual a 7
for i in range(len(list_medias)):
    if list_medias[i] >= 7:
        print(f"Aluno {i + 1:02d} com média maior ou igual a 7: {list_medias[i]:.1f}") # Printa os alunos com média maior ou igual a 7, com uma casa decimal

#Exercicio 12 - FIM
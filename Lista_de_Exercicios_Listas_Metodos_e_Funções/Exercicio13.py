# Exercício 13 — Idade e altura de uma turma
# Nível ●●●○
# Foram anotadas as idades e as alturas de 30 alunos. Elabore um programa que determine quantos alunos
# com mais de 13 anos possuem altura inferior à média de altura da turma.

import random

list_idades = []
list_alturas = []

for i in range(30):
    a = random.randint(10,20)  # Substituindo input por geração aleatória para fins de teste
    list_idades.append(a)
    b = random.uniform(1.5, 2.0)  # Substituindo input por geração aleatória para fins de teste
    print(f"Idade digitada: {a}, Altura digitada: {b:.2f}")  # Exibe a altura gerada
    list_alturas.append(b)

# Médias da altura dos alunos
sum_altura = 0
for i in range(len(list_alturas)):
    sum_altura += list_alturas[i]
media_altura = sum_altura / len(list_alturas)

# Alunos com mais de 13 anos e com altura menor que a média da altura da turma
for i in range(len(list_idades)):
    if list_idades[i] >= 13 and list_alturas[i] <= media_altura:
        print(f"Aluno {i:02d} tem {list_idades[i]:02d} anos e altura {list_alturas[i]:.1f}, sendo altura menor que a media {media_altura:.1f}")

#Exercicio 13 - FIM
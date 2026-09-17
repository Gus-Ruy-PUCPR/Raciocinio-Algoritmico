# Exercício 3 — Notas e média
# Adriel Guilherme de Paula Oliveira - 09/09/2026

# Criar uma lista para armazenar as quatro notas do aluno
notas = []

# Ler as quatro notas e armazená-las na lista
for i in range(4):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)

# Calcular a soma das notas
soma = 0

for i in range(4):
    soma = soma + notas[i]

# Calcular a média aritmética simples
media = soma / 4

# Exibir as notas digitadas
print("\nNotas digitadas:")

for i in range(4):
    print(notas[i])

# Exibir a média com duas casas decimais
print("Média: {:.2f}".format(media))

#Exercicio 03 - FIM

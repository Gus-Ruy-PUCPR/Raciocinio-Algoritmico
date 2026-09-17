# Exercício 12 — Agrupamento de estudantes por turma
# Contexto. A secretaria recebe a matrícula como pares (estudante, turma) e precisa gerar as listas de chamada por
# turma.
# Tarefa. Converta a lista de pares em um dicionário turma → lista de estudantes usando setdefault(). Exiba as
# turmas em ordem alfabética com a quantidade de estudantes e implemente também a versão equivalente com
# if/in, comprovando que os resultados são iguais.
# Requisitos técnicos:
# ● Usar setdefault(chave, []).append(...)
# ● Percorrer com sorted()
# ● Comparar os dois dicionários com ==

# Lista pre-inputada
estudantes_turmas = [
    ("Ana Clara Silva", "Turma A"),
    ("Bruno Souza Santos", "Turma A"),
    ("Carlos Eduardo Lima", "Turma A"),
    ("Daniela Costa Pereira", "Turma A"),
    ("Enzo Gabriel Rocha", "Turma A"),
    ("Fernanda Alves Martins", "Turma B"),
    ("Gabriel Henrique Ribeiro", "Turma B"),
    ("Helena Carvalho Araujo", "Turma B"),
    ("Igor Matheus Barbosa", "Turma B"),
    ("Julia Beatriz Mendes", "Turma B"),
    ("Kaique Vinicius Duarte", "Turma C"),
    ("Larissa Nicole Farias", "Turma C"),
    ("Lucas Gabriel Nogueira", "Turma C"),
    ("Mariana Vitoria Castro", "Turma C"),
    ("Nicolas Rafael Moretti", "Turma C")
]

dictionary = {}

for nome, turma in estudantes_turmas:
    dictionary.setdefault(turma, []).append(nome)

print()
print("-"*138)
print(f"Truma A: {dictionary['Turma A']}")
print("-"*138)
print(f"Truma B: {dictionary['Turma B']}")
print("-"*138)
print(f"Truma C: {dictionary['Turma C']}")
print("-"*138)
print()
# Exercício 24 — Catraca da sala de aula
# Contexto. A catraca registra (matrícula, data) a cada entrada, mas às vezes lê o crachá duas vezes no mesmo dia.
# A frequência mínima é de 75%.
# Tarefa. Descarte as leituras duplicadas usando a tupla (matrícula, data) como chave, conte as presenças por
# estudante e calcule a frequência percentual sobre o total de encontros, sinalizando quem está em risco de
# reprovação por falta.
# Requisitos técnicos:
# ● Usar tupla como chave para eliminar duplicidade
# ● Contar as presenças em um segundo dicionário
# ● Aplicar o limite de 75%

# Lista de registros brutos da catraca (com duplicatas no mesmo dia)

logs_catraca = [
    ("2023101", "2026-06-01"),
    ("2023101", "2026-06-01"),  # Duplicata
    ("2023103", "2026-06-01"),
    ("2023101", "2026-06-02"),
    ("2023102", "2026-06-02"),
    ("2023102", "2026-06-02"),  # Duplicata
    ("2023103", "2026-06-02"),
    ("2023101", "2026-06-03"),
    ("2023103", "2026-06-03"),
    ("2023101", "2026-06-04"),
    ("2023102", "2026-06-04"),
    ("2023103", "2026-06-04")
]
contador = 0
taxa_d_presenca = 0.75
aula= 0

for i in range(len(logs_catraca)):
    if contador > 0:
        if logs_catraca[i][1] == logs_catraca[i-1][1]:
            continue
        aula += 1
    contador += 1

logs_presencas = {}

for i, j in logs_catraca:
    if i not in logs_presencas:
        logs_presencas[i] = {"Matricula": i,"Presença": 1, "Data": j}
        continue
    
    if j not in logs_presencas[i]["Data"]:
        logs_presencas[i]["Presença"] += 1
        logs_presencas[i]["Data"] += f", {j}"
    
print("-"*120)
for i in logs_presencas.keys():
    if logs_presencas[i]["Presença"] < taxa_d_presenca * aula:
        print(f"Reprovados por faltas: {logs_presencas[i]}")
        print("-"*120)
    else:
        print(f"Aprovados: {logs_presencas[i]}")
        print("-"*120)
    print()
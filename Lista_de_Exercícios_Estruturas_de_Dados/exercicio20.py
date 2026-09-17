# Exercício 20 — Telemetria das salas do câmpus
# Contexto. Sensores enviam leituras de temperatura identificadas pela sala. A manutenção precisa de um resumo
# por ambiente, com alerta acima de 26 °C.
# Tarefa. Converta a lista de tuplas (sala, temperatura) em um resumo por sala contendo quantidade de leituras,
# média, mínima e máxima, sinalizando os ambientes que ultrapassaram o limite.
# Requisitos técnicos:
# ● Inicializar o acumulador na primeira ocorrência da sala
# ● Atualizar mínima e máxima dentro do laço
# ● Desempacotar o valor composto no for

# Leituras pre-inputadas
leituras_salas = [
    ("Sala 101 - Reuniões", 23.5),
    ("Sala 101 - Reuniões", 24.0),
    ("Sala 101 - Reuniões", 26.1),
    ("Sala 101 - Reuniões", 26.0),
    ("Sala 101 - Reuniões", 25.8),
    
    ("Sala 102 - Servidores", 27.2),
    ("Sala 102 - Servidores", 28.5),
    ("Sala 102 - Servidores", 29.0),
    ("Sala 102 - Servidores", 26.5),
    ("Sala 102 - Servidores", 25.8),
    
    ("Sala 103 - Diretoria", 23.0),
    ("Sala 103 - Diretoria", 24.5),
    ("Sala 103 - Diretoria", 26.8),
    ("Sala 103 - Diretoria", 27.4),
    ("Sala 103 - Diretoria", 25.2)
]

resumo_salas = {}
alertas = []

for sala, temperatura in leituras_salas:
    if temperatura >= 26.0:
        alertas += [sala, temperatura]

    if sala not in resumo_salas:
        resumo_salas[sala] = {
            "Temperatura Mínima": temperatura,
            "Temperatura Máxima": temperatura,
            "Temperatura Média": 0,
            "Quantidade": 1,
            "Soma": temperatura
            }
    else:
        if resumo_salas[sala]["Temperatura Mínima"] > temperatura:
            resumo_salas[sala]["Temperatura Mínima"] = temperatura
        if resumo_salas[sala]["Temperatura Máxima"] < temperatura:
            resumo_salas[sala]["Temperatura Máxima"] = temperatura

        resumo_salas[sala]["Quantidade"] += 1
        resumo_salas[sala]["Soma"] += temperatura

for sala in resumo_salas:
    resumo_salas[sala]["Temperatura Média"] = resumo_salas[sala]["Soma"] / resumo_salas[sala]["Quantidade"]
    resumo_salas[sala].pop("Soma", "Chave inexistente")
    resumo_salas[sala].pop("Quantidade", "Chave inexistente")

print()
print("-"*50)
for key, value in resumo_salas.items():
    print(f"Salas: {key}\nTemperaturas: {value}")
    print("-"*50)

print()
print("-"*50)
print("Alertas de temperatura!")
for i in range(len(alertas)):
    print(f"{alertas[i]}")
print()

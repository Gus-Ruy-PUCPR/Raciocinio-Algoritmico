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
    # Sala 101 - Reuniões
    ("Sala 101", 22.5),
    ("Sala 101", 23.0),
    ("Sala 101", 24.1),
    ("Sala 101", 25.0),
    ("Sala 101", 24.8),
    
    # Sala 102 - Servidores (com temperaturas elevadas gerando alerta)
    ("Sala 102", 27.2),
    ("Sala 102", 28.5),
    ("Sala 102", 29.0),
    ("Sala 102", 26.5),
    ("Sala 102", 25.8),
    
    # Sala 103 - Diretoria (com temperaturas mistas)
    ("Sala 103", 23.0),
    ("Sala 103", 24.5),
    ("Sala 103", 26.8),
    ("Sala 103", 27.4),
    ("Sala 103", 25.2)
]

resumo_salas = {}
alertas = []
i = 1
for sala, temperatura in leituras_salas:
    if temperatura >= 26.0:
        alertas += [sala, temperatura]

    if sala not in resumo_salas:
        resumo_salas[sala] = {"Temperatura Mínima": temperatura, "Temperatura Máxima": temperatura, "Temperatura Média": 0, "Quantidade": 1, "Soma": temperatura}
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

print()
print("-"*50)
for i in range(len(alertas)):
    print("Alertas de temperatura!")
    print(f"Salas: {alertas[i][0]}\nTemperaturas: {alertas[i][1]}")
    print("-"*50)
print()

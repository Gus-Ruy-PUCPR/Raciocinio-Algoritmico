# Exercício 11 - Thiago Augusto da Silva - 18/09
# CONTEXTO: O totem de autoatendimento consulta ramais. Se o setor não existir, o totem não pode travar: precisa
# informar que o ramal não está cadastrado.
# TAREFA: Monte o dicionário de ramais e consulte uma lista de setores, alguns inexistentes, usando get() com valor
# padrão. Ao final, compare o comportamento de get() com o do acesso direto por colchetes, tratando a exceção
# Requisitos técnicos:
# ● Usar get() com segundo argumento
# ● Normalizar a busca com lower()
# ● Demonstrar o KeyError em bloco try/except

# 1. Criação do dicionário de ramais do câmpus
ramais_campus = {
    "secretaria": "3211",
    "biblioteca": "3212",
    "coordenação": "3213",
    "laboratório de informática": "3214",
    "recursos humanos": "3215"
}

# Lista de setores para consulta (incluindo alguns inexistentes e com variações de maiúsculas)
consultas = ["Secretaria", "Financeiro", "BIBLIOTECA", "Almoxarifado"]

print("--- 1. CONSULTA SEGURA COM GET() ---")
# 2. Busca normalizada usando get() com valor padrão
for setor in consultas:
    # Normaliza a busca para minúsculas
    setor_normalizado = setor.lower()
    
    # Consulta usando get(chave, valor_padrao)
    ramal = ramais_campus.get(setor_normalizado, "Ramal não cadastrado")
    print(f"Setor: {setor} -> Ramal: {ramal}")


print("\n--- 2. COMPARAÇÃO COM ACESSO DIRETO [] E TRATAMENTO DE EXCEÇÃO ---")
# 3. Demonstração do comportamento com colchetes e tratamento de KeyError
for setor in consultas:
    setor_normalizado = setor.lower()
    
    try:
        # Tenta o acesso direto por colchetes
        ramal = ramais_campus[setor_normalizado]
        print(f"Setor: {setor} -> Ramal: {ramal}")
    except KeyError:
        # Trata o erro caso a chave (setor) não exista no dicionário
        print(f"Setor: {setor} -> Erro: O setor não foi encontrado (KeyError tratado)!")
# Exercício 11 - Fim
# Exercício 13 - Thiago Augusto da Silva - 18/09
# CONTEXTO: Um lote de cancelamentos chega do sistema acadêmico. Algumas matrículas do lote já não existem
# mais — e isso não pode derrubar o processamento.
# TAREFA: Processe a lista de cancelamentos com pop() e valor padrão, informando o que foi cancelado e o que não
# foi encontrado. Ao final, demonstre por que del exigiria verificação prévia.
# Requisitos técnicos:
# ● Usar pop(chave, None)
# ● Testar o retorno com is None
# ● Proteger o del com if chave in dicionario

# Criação do dict e da lista de cancelamentos
matriculasAtivas = {
    "MAT100": "Ana Silva",
    "MAT101": "Bruno Costa",
    "MAT102": "Carlos Souza",
    "MAT103": "Diana Oliveira",
    "MAT104": "Thiago Augusto",
    "MAT105": "Gabriel Santos"
}

cancelamentos = ("MAT100", "MAT103", "MAT106", "MAT109")

# Processando a lista com pop()
for matricula in cancelamentos:
    resultado = matriculasAtivas.pop(matricula, None) # Verificamos se a matricula ainda existe de fato, caso nao, informamos o usuario
    if resultado is None:
        print(f"Matrícula {matricula} não foi encontrada!")
    else:
        print(f"Inscrição de {resultado} ({matricula}) foi cancelada com sucesso!")
print("\nMatrículas ativas restantes:", matriculasAtivas)

# Restaurando o dict para demonstrar o caso com del()
matriculasAtivas = {
    "MAT100": "Ana Silva",
    "MAT101": "Bruno Costa",
    "MAT102": "Carlos Souza",
    "MAT103": "Diana Oliveira",
    "MAT104": "Thiago Augusto",
    "MAT105": "Gabriel Santos"
}

for matricula in cancelamentos:
    try: # Alternativamente, poderiamos realizar uma verificação previa usando um argumento tal como "if matricula in matriculasAtivas" para evitar o erro
        del matriculasAtivas[matricula]
        print(f"Matricula {matricula} removida com sucesso!")
    except(KeyError): # Ao tentar remover algo que não existe, o argumento Del() retorna KeyError
        print(f"Falha ao tentar remover a matricula! Esta matricula não existe mais!")
# Exercício 13 - Fim
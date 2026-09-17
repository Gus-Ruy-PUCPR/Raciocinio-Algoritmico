# Exercício 8 — Funcionário e dependentes
# Contexto. O RH cadastra o funcionário e vai incluindo os dependentes um a um, conforme a documentação é
# apresentada.
# Tarefa. Partindo de uma tupla vazia, acrescente dinamicamente cada dependente com o operador += e exiba, ao
# final, a ficha completa numerada.
# Requisitos técnicos:
# ● Iniciar com tupla vazia
# ● Usar += com tupla de um elemento (atenção à vírgula)
# ● Numerar a saída com enumerate

cad_funcionario = ()
i = 0
# Loop de adção a tupla
while len(cad_funcionario) < 5:
    dep = input(f"Nome do dependente a ser inserido na tupla? ({i+1}/5)\n")
    i += 1
    # concatenação
    cad_funcionario += (dep,)

# Quebra de linha
print()

# Print com enumerate
for i in enumerate(cad_funcionario):
    print(i)
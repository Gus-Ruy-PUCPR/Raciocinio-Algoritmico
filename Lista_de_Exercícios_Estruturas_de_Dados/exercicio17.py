# Exercício 17 - Thiago Augusto da Silva - 18/09
# CONTEXTO: O varejo aplicará 8% de reajuste, mas a tabela atual precisa ser preservada para efeito de auditoria.
# TAREFA: Gere um novo dicionário com os preços reajustados usando compreensão de dicionário e outro apenas
# com os itens abaixo de R$ 100. Exiba a comparação lado a lado e comprove que o dicionário original não foi
# alterado.
# Requisitos técnicos:
# ● Usar compreensão de dicionário com e sem filtro
# ● Arredondar com round(valor, 2)
# ● Comprovar a preservação do original

tabelaAtual = {
    "CachorroQuente": float(10.20),
    "BauruSimples": float(10.30),
    "BauruOvo": float(11.50),
    "Hamburger": float(15.20),
    "Cheeseburger": float(17.30),
    "Refrigerante": float(10.00),
    "Beef Wellington": float(100.25),
    "PratoExecutivo": float(80.50),
    "Strogonoff": float(66.30),
    "Alcatra": float(125.50)
}

tabelaNova = { # Novo dicionario com novos valores
    item: round(preco * 1.08, 2) for item, preco in tabelaAtual.items()
}
tabelaAbaixo100 = { # Criação do dicionário com apenas itens abaixo de R$ 100
    item: preco for item, preco in tabelaNova.items() if preco < 100.00
}

# Comparação lado a lado, comprovando que mantemos a tabela original
print(f"{'Item':<20} | {'Original':^10} | {'Reajustado':^10}")
for item, preco in tabelaAtual.items():
    valorOriginal = str(f"R$ {tabelaAtual[item]:.2f}")
    valorNovo = str(f"R$ {tabelaNova[item]:.2f}")
    print(f"{item:<20} | {valorOriginal:^10} | {valorNovo:^10}")

print("\nItens abaixo de R$100\n")
for item,preco in tabelaAbaixo100.items():
    print(f"{item:<15}: {preco}")
# Exercício 17 - Fim
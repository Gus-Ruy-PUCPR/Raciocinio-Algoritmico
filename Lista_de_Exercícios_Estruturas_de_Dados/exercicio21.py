# Exercício 21 - Thiago Augusto da Silva - 18/09
# CONTEXTO: Toda aplicação tem uma configuração de fábrica que pode ser sobreposta pelas preferências do usuário
# — sem que a configuração de fábrica se perca.
# TAREFA: Combine os dois dicionários com o operador | e, alternativamente, com copy() e update(). Comprove que
# os resultados são equivalentes, que o padrão foi preservado e liste as chaves personalizadas com o valor antigo e
# o novo.
# Requisitos técnicos:
# ● Usar o operador | (Python 3.9+)
# ● Comparar com update() sobre uma cópia
# ● Percorrer as personalizações com items()

padrao = {"tema": "claro", "idioma": "pt-BR", "notificacoes": True, "timeout": 30}
usuario = {"tema": "escuro", "timeout": 60}

# Python 3.9+: o operador | cria um NOVO dicionario
efetiva = padrao | usuario
print("Padrão :", padrao)
print("Usuário:", usuario)
print("Efetiva:", efetiva)
print("O padrão foi preservado?", padrao["tema"] == "claro")

# update() altera o dicionario existente (in place)
copia = padrao.copy()
copia.update(usuario)
print("Com update():", copia)
print("Resultados equivalentes?", copia == efetiva)

# Quais chaves o usuario personalizou?
print("\nPersonalizações:")
for chave, valor in usuario.items():
    print(f" {chave}: {padrao[chave]} -> {valor}")
    
# Exercício 21 - Fim
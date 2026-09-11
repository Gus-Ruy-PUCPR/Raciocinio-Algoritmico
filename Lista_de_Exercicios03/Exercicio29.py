# Exercício 29 - Lista de Exercícios 03
PRECO_UNITARIO = 1.99

print("Lojas Quase Dois - Tabela de precos")

# Gera a tabela de 1 a 50 produtos
for quantidade in range(1, 51):
    total = quantidade * PRECO_UNITARIO
    print(f"{quantidade} - R$ {total:.2f}")
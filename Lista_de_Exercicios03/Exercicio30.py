# Exercício 30 - Lista de Exercícios 03
# Leitura e validação do preço unitário do pão
preco_unitario = float(input("Preço do pão: R$ "))
while preco_unitario <= 0:
    print("Erro: O preço deve ser maior que zero.")
    preco_unitario = float(input("Preço do pão: R$ "))

print("\nPanificadora Pão de Ontem - Tabela de preços")

# Gera a tabela de 1 a 50 pães
for quantidade in range(1, 51):
    total = quantidade * preco_unitario
    print(f"{quantidade} - R$ {total:.2f}")
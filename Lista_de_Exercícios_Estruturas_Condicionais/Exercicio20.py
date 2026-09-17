# 20. Hipermercado Tabajara — cupom fiscal
# O Hipermercado Tabajara trabalha com a seguinte tabela de preços de carnes, na qual o preço por quilo varia
# conforme a quantidade adquirida:

# Tipo de carne          Até 5 kg         Acima de 5 kg
# Filé duplo             R$ 4,90 por kg   R$ 5,80 por kg
# Alcatra                R$ 5,90 por kg   R$ 6,80 por kg
# Picanha                R$ 6,90 por kg   R$ 7,80 por kg

# Cada cliente pode levar apenas um dos tipos de carne, porém não há limite para a quantidade. Se a compra
# for feita no cartão Tabajara, o cliente recebe ainda um desconto de 5% sobre o total da compra. Escreva um
# programa que peça o tipo e a quantidade de carne comprada, bem como a forma de pagamento, e gere um
# cupom fiscal contendo o tipo e a quantidade de carne, o preço total, o tipo de pagamento, o valor do
# desconto e o valor a pagar.

carne = input("Qual carne vai levar? (Picanha-P / Filé Duplo-F / Alcatra-A) ")
carne = carne.upper()
quantidade = float(input("Quantos quilos de carne? "))
cartao = input("Pagamento no cartão Tabajara? (s/n): ")
cartao = cartao.upper()

if carne not in ["P", "F", "A"]:
    print("Entrada Inválida!!!")
    exit()

if carne == "F":
    nome_carne = "File Duplo"
    if quantidade <= 5:
        preco_kg = 4.90
    else:
        preco_kg = 5.80
elif carne == "A":
    nome_carne = "Alcatra"
    if quantidade <= 5:
        preco_kg = 5.90
    else:
        preco_kg = 6.80
else:
    nome_carne = "Picanha"
    if quantidade <= 5:
        preco_kg = 6.90
    else:
        preco_kg = 7.80

valor_total = quantidade * preco_kg

if cartao == "S":
    desconto = valor_total * 0.05
    tipo_pagamento = "Cartão Tabajara (5% de desconto)"
else:
    desconto = 0.0
    tipo_pagamento = "Outro meio de pagamento"

valor_a_pagar = valor_total - desconto

print(f"Tipo de carne:       {nome_carne}")
print(f"Quantidade:          {quantidade} kg")
print(f"Preço total:         R$ {valor_total:.2f}")
print(f"Tipo de pagamento:   {tipo_pagamento}")
print(f"Valor do desconto:   R$ {desconto:.2f}")
print(f"Valor a pagar:       R$ {valor_a_pagar:.2f}")
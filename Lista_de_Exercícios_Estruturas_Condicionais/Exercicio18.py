# 18. Posto de combustíveis
# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#
# Combustível     Até 20 litros               Acima de 20 litros
# Álcool          desconto de 3% por litro    desconto de 5% por litro
# Gasolina        desconto de 4% por litro    desconto de 6% por litro
#
# Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte
# forma: A para álcool, G para gasolina), calcule e imprima o valor a ser pago pelo cliente, sabendo que o preço
# do litro da gasolina é R$ 2,50 e o preço do litro do álcool é R$ 1,90. Códigos de combustível diferentes de A e
# G devem ser rejeitados.

a_or_g = input("Qual combustível sera abastecido? (Álcool-A/Gasolina-G) ")
litros = float(input("Quantos litros sarão abastecidos? "))
a_or_g = a_or_g.upper()
v_gas  = float(2.50)
v_alc  = float(1.90)

if a_or_g == "A":
    desconto = 0.03 if litros <= 20 else 0.05
    valor_total = litros * v_alc
    valor_pag = valor_total - valor_total * desconto
    combustivel = "Gasolina"
elif a_or_g == "G":
    desconto = 0.04 if litros <= 20 else 0.06
    valor_total = litros * v_gas
    valor_pag = valor_total - valor_total * desconto
    combustivel = "Álcool"
else:
    print(f"Código inválido inserido (Valor inserido: {a_or_g})! Insira A ou G.")
    exit()

print(f"Litros:      {litros}")
print(f"Combustivel: {combustivel}")
print(f"Valor Total: {valor_pag}")
print(f"Desconto:    {valor_total - valor_pag:.2f}")
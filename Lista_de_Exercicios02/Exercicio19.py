# 19. Fruteira
# Uma fruteira está vendendo frutas com a seguinte tabela de preços, na qual a faixa de preço é definida
# separadamente para cada fruta, conforme a quantidade adquirida daquela fruta:

# Fruta           Até 5 kg          Acima de 5 kg
# Morango         R$ 2,50 por kg    R$ 2,20 por kg
# Maçã            R$ 1,80 por kg    R$ 1,50 por kg

# Se o cliente comprar mais de 8 kg de frutas no total ou se o valor total da compra ultrapassar R$ 25,00, ele
# receberá ainda um desconto de 10% sobre esse total. Escreva um algoritmo para ler a quantidade (em kg)
# de morangos e a quantidade (em kg) de maçãs adquiridas e escrever o valor a ser pago pelo cliente.

morango = float(input("Quantos kilos de morango? "))
maca    = float(input("Quantos kilos de maca? "))

if morango < 5:
    preco_morango = morango * 2.50
else:
    preco_morango = morango * 2.20

if maca < 5:
    preco_maca = maca * 1.80
else:
    preco_maca = maca * 1.50

if maca + morango == 8 or preco_maca + preco_morango == 25:
    total = (preco_morango + preco_maca) * 0.9
else:
    total = preco_maca + preco_morango

print(f"Maça:        {maca} Kg")
print(f"Morango:     {morango} Kg")
print(f"Valor total: {total} R$")
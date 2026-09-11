# Exercício 22 — Comparativo de consumo de combustível. Sarah Gabrielli Rodrigues de Souza Ribeiro - 09/09/2026.
# Carregar uma lista com modelos de cinco carros e outra com o consumo deles, quantos km/l eles percorrem. 
# Calcular e exibir:
# A) O modelo do carro mais econômico citado.
# B) Quantos litros cada um consome para percorrer 1.000 km e quanto custará — gasolina R$ 6,19 litro.

ModelosCarros = []
ConsumosCarros = []

for i in range(5):
    ModeloCarro = input("Por gentileza, digite o modelo do " + str(i+1) + "° carro: ")
    ConsumoCarro = float(input("Por gentileza, digite o seu consumo em km/l logo em seguida: "))

    ModelosCarros.append(ModeloCarro)
    ConsumosCarros.append(ConsumoCarro)

MaiorConsumo = ConsumosCarros[0]
PosiçãoMaior = 0

for i in range(1, 5):

    if ConsumosCarros[i] > MaiorConsumo:

        MaiorConsumo = ConsumosCarros[i]
        PosiçãoMaior = i

print("\033[1mRelatório Final:\033[0m") # Deixei em negrito para ficar bonitinho.

for i in range(5):

    Litros = 1000 / ConsumosCarros[i]
    Custo = Litros * 6.19

    print( i + 1,".", ModelosCarros[i], "-", ConsumosCarros[i], "-",
          f"{Litros:.1f}", "litros • R$", f"{Custo:.2f}")

print("O carro de menor consumo é do(a)", ModelosCarros[PosiçãoMaior] + ".")

# Exercício 22 - FIM.
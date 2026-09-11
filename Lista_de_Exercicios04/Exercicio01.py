# Exercício 01 — Leitura e exibição de uma lista. Sarah Gabrielli Rodrigues de Souza Ribeiro - 07/09/2026.
# Ler uma lista de 5 números, exibir todos os valores lidos. No fim mostrar a lista completa em uma linha.
Numeros = [0, 0, 0, 0, 0]
for i in range(len(Numeros)):
    Num = int(input("Por gentileza, digite um número: "))
    Numeros [i] = Num
for i in range(5):
    print("No índice:", i, "o seu devido valor é:", Numeros[i])

print("Esta é a lista", Numeros)

# Exercício 01 - FIM.

# Variáveis com a primeira letra maiúscula não é recomendado. Pois no futuro aprenderemos sobre classes, e por conveniência classes tem a primeira letra como maiúscula. 
# Então, para não confundir, é melhor sempre usar a primeira letra minúscula para variáveis.   
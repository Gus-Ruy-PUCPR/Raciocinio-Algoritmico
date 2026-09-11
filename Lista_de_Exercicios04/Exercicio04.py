# Exercício 4 — Contagem de consoantes
# Adriel Guilherme de Paula Oliveira - 09/09/2026

# Criar uma lista para armazenar os 10 caracteres
caracteres = []

# Ler os 10 caracteres
for i in range(10):
    caractere = input("Digite um caractere: ")
    caracteres.append(caractere)

# Lista contendo somente as consoantes válidas
consoantes = "bcdfghjklmnpqrstvwxyz"

# Contador de consoantes
quantidade = 0

# Percorrer a lista e verificar cada caractere
for i in range(10):
    caractere = caracteres[i].lower()

    # Verificar se o caractere possui apenas uma letra
    # e se pertence ao conjunto de consoantes
    if len(caractere) == 1:
        if caractere in consoantes:
            quantidade = quantidade + 1

# Exibir a quantidade de consoantes
print("\nQuantidade de consoantes:", quantidade)

# Exibir as consoantes encontradas
print("Consoantes lidas:")

for i in range(10):
    caractere = caracteres[i].lower()

    if len(caractere) == 1:
        if caractere in consoantes:
            print(caractere)

#Exercicio 04 – FIM 

# Caracteres com mais de uma letra não são considerados válidos. Portanto, se o usuário digitar "ab", "abc" ou qualquer outra sequência de letras,
# isso não será contado como consoante. Apenas caracteres individuais que sejam consoantes serão contabilizados.
# Assim como números, símbolos ou espaços não serão considerados consoantes válidas, mas são considerados caracteres.
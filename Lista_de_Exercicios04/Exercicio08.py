# Exercício 08 - Thiago Augusto da Silva - 01/09
# Elabore um programa que leia a idade e a altura de 5 pessoas, armazenando cada informação em sua
# respectiva lista. Ao final, mostre a idade e a altura de cada pessoa na ordem inversa à da leitura.
# Observe que as duas listas são paralelas: o índice i identifica a mesma pessoa nas duas.

alturas = []
nomes = []

for i in range(5):
            entrada = float(input(f"Digite a {i+1}a altura, em metros: "))
            alturas.append(entrada)
            entrada = str(input(f"Digite o {i+1}o nome: "))
            nomes.append(entrada)
print("--------------------")
print("Nomes - Alturas")
for i in range(4, -1, -1):
    print(f"{nomes[i]} - {alturas[i]}m")
print("--------------------")

# Exercício 08 - Fim
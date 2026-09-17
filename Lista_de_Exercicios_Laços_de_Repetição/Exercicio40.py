#  Exercício 40 - Lista de Exercícios 03

soma_veiculos = 0
soma_acidentes = 0
quantidade_menor_2000 = 0
for contador in range(5):
    codigo = int(input("Código da cidade: "))
    veiculos = int(input("Número de veículos: "))
    acidentes = int(input("Número de acidentes: "))
    while veiculos < 0 or acidentes < 0:
        print("Os valores não podem ser negativos!")
        veiculos = int(input("Número de veículos: "))
        acidentes = int(input("Número de acidentes: "))
    soma_veiculos = soma_veiculos + veiculos
    if contador == 0:
        maior = acidentes
        menor = acidentes
        cidade_maior = codigo
        cidade_menor = codigo
    else:
        if acidentes > maior:
            maior = acidentes
            cidade_maior = codigo
        if acidentes < menor:
            menor = acidentes
            cidade_menor = codigo
    if veiculos < 2000:
        soma_acidentes = soma_acidentes + acidentes
        quantidade_menor_2000 = quantidade_menor_2000 + 1
media_veiculos = soma_veiculos / 5
print("Maior número de acidentes:", maior)
print("Código da cidade:", cidade_maior)
print("Menor número de acidentes:", menor)
print("Código da cidade:", cidade_menor)
print("Média de veículos:", round(media_veiculos, 2))
if quantidade_menor_2000 > 0:
    media_acidentes = soma_acidentes / quantidade_menor_2000
    print("Média de acidentes nas cidades com menos de 2000 veículos:",
          round(media_acidentes, 2))
else:
    print("Nenhuma cidade possui menos de 2000 veículos.")

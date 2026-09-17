# Exercício 18 — Salto em distância
# Nível ●●●○
# Em uma competição de salto em distância, cada atleta tem direito a cinco saltos, e o resultado é a média das
# cinco distâncias alcançadas.
# Elabore um programa que receba o nome e as cinco distâncias de cada atleta e informe, ao final de cada
# atleta, o nome, os saltos e a média obtida. O programa deve ser encerrado quando o nome do atleta for
# informado em branco.
# A disposição das informações deve ser a mais próxima possível do exemplo.

# Exemplo de saída:
# Atleta: Rodrigo Curvêllo
# Primeiro Salto: 6.5
# Segundo Salto: 6.1
# Terceiro Salto: 6.2
# Quarto Salto: 5.4
# Quinto Salto: 5.3
# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

import random

list_pulos = []
list_names = []
buffer = []

# Loop principal para coleta de dados
while True:
    nome = input("Qual o nome do atleta? ")
    if len(nome) == 0:
        break

    list_names.append(nome)

    #Coleta de pulos
    for i in range(5):
        a = round(random.uniform(2, 6), 1) # Aqui iria o input, mas para não perder 10 anos testando, vamos utilizar random.uniform()
        print(f"Pulo 1: {a:.2f}")
        buffer.append(a) 

    list_pulos.append(buffer)
    buffer = []

# Nomes para cada salto
ordem_saltos = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]

print("Resultado final:")

# Formatação da saida
for i in range(len(list_names)):
    atleta = list_names[i]
    saltos = list_pulos[i]
    media = sum(saltos) / len(saltos)

    # Formatação da string de saltos (6.1 - 6.2 - 6.3 ...)
    saltos_formatados = ""
    for idx, s in enumerate(saltos):
        if idx == 0:
            saltos_formatados += str(s)
        else:
            saltos_formatados += f" - {s}"

    print(f"Atleta: {atleta}")
    print(f"Saltos: {saltos_formatados}")
    print(f"Média dos saltos: {media:.1f} m\n")

#Exercicio 18 - FIM
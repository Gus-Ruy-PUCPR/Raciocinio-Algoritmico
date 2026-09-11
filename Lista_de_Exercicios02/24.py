# 24. Investigação criminal
# Faça um programa que faça cinco perguntas a uma pessoa sobre um crime, respondidas com S (sim) ou N
# (não):
# • "Telefonou para a vítima?"
# • "Esteve no local do crime?"
# • "Mora perto da vítima?"
# • "Devia para a vítima?"
# • "Já trabalhou com a vítima?"
# Ao final, o programa deve emitir uma classificação sobre a participação da pessoa no crime, com base na
# quantidade de respostas positivas: exatamente 2 respostas positivas classificam a pessoa como Suspeita; 3
# ou 4 respostas positivas, como Cúmplice; 5 respostas positivas, como Assassino. Nos demais casos (0 ou 1
# resposta positiva), a pessoa é classificada como Inocente.
# Sem laços de repetição, a contagem deve ser feita por acumulação: uma variável contadora, incrementada dentro
# de cada decisão.

print("Responda às perguntas seguintes com 'S' para Sim ou 'N' para Não.\n")

contador = 0

p1 = input("Telefonou para a vítima? (S/N): ").strip().upper()
if p1 == "S":
    contador = contador + 1
elif p1 != "N":
    print("Entrada inválida. Responda apenas com S ou N.")
    contador = -1

if contador != -1:
    p2 = input("Esteve no local do crime? (S/N): ").strip().upper()
    if p2 == "S":
        contador = contador + 1
    elif p2 != "N":
        print("Entrada inválida. Responda apenas com S ou N.")
        contador = -1

if contador != -1:
    p3 = input("Mora perto da vítima? (S/N): ").strip().upper()
    if p3 == "S":
        contador = contador + 1
    elif p3 != "N":
        print("Entrada inválida. Responda apenas com S ou N.")
        contador = -1

if contador != -1:
    p4 = input("Devia para a vítima? (S/N): ").strip().upper()
    if p4 == "S":
        contador = contador + 1
    elif p4 != "N":
        print("Entrada inválida. Responda apenas com S ou N.")
        contador = -1

if contador != -1:
    p5 = input("Já trabalhou com a vítima? (S/N): ").strip().upper()
    if p5 == "S":
        contador = contador + 1
    elif p5 != "N":
        print("Entrada inválida. Responda apenas com S ou N.")
        contador = -1

if contador == -1:
    print("Programa encerrado devido a entrada(s) inválida(s).")
else:
    print("\nResultado da Investigação")
    print(f"Total de respostas 'Sim': {contador}")
    
    if contador == 2:
        print("Classificação: SUSPEITA")
    elif contador == 3 or contador == 4:
        print("Classificação: CÚMPLICE")
    elif contador == 5:
        print("Classificação: ASSASSINO")
    else:
        print("Classificação: INOCENTE")
# Exercício 15 - Thiago Augusto da Silva - 01/09
# Elabore um programa que faça a uma pessoa as cinco perguntas a seguir, armazenando as respostas em uma
# lista:
# a) Telefonou para a vítima? - b) Esteve no local do crime? -  c) Mora perto da vítima? - d) Devia para a vítima?
# e) Já trabalhou com a vítima?
# O programa deve aceitar apenas as respostas S e N, repetindo a pergunta em caso de resposta inválida. Ao
# final, emita a classificação da participação da pessoa conforme a tabela abaixo.

probabilidade = []
classificacao = str()
respostasValidas = str("SsNn")
contadorProbabilidade = int(0)
perguntas = ["\nVocê telefonou a vítima do crime?\n", "\nEsteve no local do crime?\n", "\nVocê mora perto da vítima?\n", "\nVocê devia algo para a vítima?\n", "\nVocê já trabalhou com a vítima?\n"]

nome = str(input("Por favor insira o seu nome: "))
print("Por favor responda as seguintes perguntas com sim (S) ou não (N)")

for i in range(5): # Evita a necessidade de fazer todas as perguntas em funções diferentes
    while True: 
        resposta = str(input(f"{perguntas[i]}"))
        if resposta not in respostasValidas:
            print("Por favor responda apenas com sim (S) ou não (N)")
        else:
            probabilidade.append(resposta)
            break

for i in range(5): # Agora contamos quantas vezes o usúario respondeu "Sim"
    if probabilidade[i] in ("Ss"):
        contadorProbabilidade += 1
        print("Contado")

if contadorProbabilidade > 1 and contadorProbabilidade < 3: classificacao = "Suspeito"
elif contadorProbabilidade > 2 and contadorProbabilidade < 5: classificacao = "Cúmplice"
elif contadorProbabilidade > 4: classificacao = "Assassino"
else: classificacao = "Inocente"
print(f"\nContabilizando respostas...\n...Você é {classificacao}!")

# Exercício 15 - Fim
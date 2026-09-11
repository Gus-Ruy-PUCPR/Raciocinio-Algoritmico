# Exercício 16 — Notas com valor sentinela. Sarah Gabrielli Rodrigues de Souza Ribeiro - 08/09/2026.
# Ler um número indeterminado de notas, encerrar quando valor -1 (não deve ser armazenado).
# Após a entrada. deve ser feito:
# A) Mostrar a quantidade de valores lidos.
# B) Exibir todos os valores na ordem em que foram informados, um ao lado do outro.
# C) Exibir todos os valores na ordem inversa, um abaixo do outro.
# D) Calcular e mostrar a soma dos valores.
# E) Calcular e mostrar a média dos valores.
# F) Calcular e mostrar a quantidade de valores acima da média calculada.
# G) Calcular e mostrar a quantidade de valores abaixo de sete.
# H) Encerrar o programa com uma mensagem.

i = 1

Notas = []

Nota = float(input(f'Por gentileza, digite a {i}° nota (Digite "-1" para encerrar): '))

while Nota != -1:
    Notas.append(Nota)
    i += 1
    Nota = float(input(f'Por gentileza, digite a {i}° nota (Digite "-1" para encerrar): '))

print("A) Esta é a quantidade de valores lidos:", len(Notas))

if len(Notas) > 0:

    print("B) Os valores na ordem informada:", end=" ")

    for i in range(len(Notas)):
        print(f"• {Notas[i]:.1f}", end=" ")

    print()

    print("C) Os valores na ordem inversa:")

    for i in range(len(Notas) - 1, -1, -1):
        print(f" • {Notas[i]:.1f}")

    Soma = 0

    for i in range(len(Notas)):
        Soma = Soma + Notas[i]

    Media = Soma / len(Notas)

    AcimaDaMedia = 0

    for i in range(len(Notas)):
        if Notas[i] > Media:
            AcimaDaMedia += 1

    AbaixoDeSete = 0

    for i in range(len(Notas)):
        if Notas[i] < 7:
            AbaixoDeSete += 1

    print(f"D) Esta é a soma dos valores: {Soma:.2f}")
    print(f"E) Esta é a média dos valores: {Media:.2f}")
    print("F) Esta é a quantidade de valores que ficaram acima da média:", AcimaDaMedia)
    print("G) Esta é a quantidade de valores que ficaram abaixo de sete:", AbaixoDeSete)

else:
    print("Perdão, nenhum valor fora informado.")

print("H) Por agora o processamento está encerrado. Lhe vejo em uma próxima vez!")

# Exercício 16 - FIM.
# 15. Conceito por faixa de Media
# Faça um programa que leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um
# semestre e calcule a sua Media. A atribuição de conceitos obedece à tabela abaixo:
# Media de aproveitamento Conceito
# de 9,0 (inclusive) até 10,0 A
# de 7,5 (inclusive) até 9,0 B
# de 6,0 (inclusive) até 7,5 C
# de 4,0 (inclusive) até 6,0 D
# de 0,0 até 4,0 E
# O programa deve mostrar na tela as notas, a Media, o conceito correspondente e a mensagem APROVADO se
# o conceito for A, B ou C, ou REPROVADO se o conceito for D ou E. Medias fora do intervalo de 0 a 10 devem ser
# rejeitadas.
# Note que os limites das faixas são fechados à esquerda e abertos à direita: uma Media exatamente igual a 9,0 recebe
# conceito A, e não B.

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2
situacao = "APROVADO"

if media < 0.0 or media > 10.0:
    print("Media inválida! Precisa estar entre 0 e 10.")
else:
    if 9.0 <= media <= 10.0:
        conceito = "A"
    elif 7.5 <= media < 9.0:
        conceito = "B"
    elif 6.0 <= media < 7.5:
        conceito = "C"
    elif 4.0 <= media < 6.0:
        conceito = "D"
        situacao = "REPROVADO"
    else:
        conceito = "E"
        situacao = "REPROVADO"

    print(f"Notas: {nota1} e {nota2}")
    print(f"Media: {media}")
    print(f"Conceito: {conceito}")
    print(f"Situação: {situacao}")
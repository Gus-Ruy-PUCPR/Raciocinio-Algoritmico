# 07. Média de duas notas
# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média
# alcançada e apresentar:
# • a mensagem Aprovado, se a média alcançada for maior ou igual a sete;
# • a mensagem Reprovado, se a média for menor do que sete;
# • a mensagem Aprovado com Distinção, se a média for igual a dez.
# Atenção à ordem dos testes: a média igual a dez também satisfaz a condição "maior ou igual a sete". Reflita sobre
# qual condição deve ser avaliada primeiro.

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2)/2

if media == 10:
    print(f"Aprovado com media: {media}. Muito bem!!!")
elif media > 7:
    print(f"Aprovado com media: {media}!")
else:
    print(f"Reprovado com media: {media}!")
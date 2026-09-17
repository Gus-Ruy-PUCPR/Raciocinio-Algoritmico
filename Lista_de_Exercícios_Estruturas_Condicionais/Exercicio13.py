# 13. Turno de estudo
# Faça um programa que pergunte em que turno o usuário estuda. Peça para digitar M (matutino), V
# (vespertino) ou N (noturno). Imprima a mensagem Bom dia!, Boa tarde!, Boa noite! ou Valor inválido!,
# conforme o caso.

turno = input("Digite o seu turno (M/V/N - Matiturno, Vespertino, Noturno)")
turno = turno.upper()

if turno == "M":
    print(f"Bom dia!!!")
elif turno == "V":
    print(f"Boa tarde!!!")
elif turno == "M":
    print(f"Boa noite!!!")
else:
    print("Entrada inválida!!!")
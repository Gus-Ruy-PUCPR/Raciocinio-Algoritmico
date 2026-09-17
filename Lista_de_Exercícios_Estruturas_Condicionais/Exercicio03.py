# 03. Classificação por sexo
# Faça um programa que verifique se uma letra digitada é F ou M e escreva, conforme a letra: F - Feminino, M
# - Masculino ou Sexo inválido. O programa deve aceitar a letra digitada tanto em maiúscula quanto em
# minúscula.

sexo = input("Digite seu sexo F/M: ")

if sexo in ["F", "f"]:
    print("Feminino!")
elif sexo in ["M", "m"]:
    print("Masculino!")
else:
    print("Inválido!!!")
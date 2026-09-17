# 04. Vogal ou consoante
# Faça um programa que verifique se uma letra digitada é vogal ou consoante. O programa deve rejeitar
# entradas que não sejam exatamente uma letra do alfabeto (dígitos, símbolos, texto vazio ou mais de um
# caractere).

letra = input("Digite uma letra: ")
letra = letra.upper()

if not letra.isalpha():
    print("Nao é letra!!!")
    exit()

if letra in ["A", "E", "I", "O", "U"]:
    print(f"{letra} é vogal!!!")
else:
    print(f"{letra} é consoante!!!")
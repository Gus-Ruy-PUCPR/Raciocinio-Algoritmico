# Exercício 03 — Ficha cadastral validada
# Nível 2 — Fundamental · Padrão algorítmico: Validação de entrada (múltiplos campos)
# Faça um programa que leia e valide, campo a campo, as seguintes informações:
# • Nome: mais de 3 caracteres
# • Idade: entre 0 e 150;
# • Salário: maior que zero;
# • Sexo: 'f' ou 'm';
# • Estado civil: 's', 'c', 'v' ou 'd'.

nome = input("Digite seu nome: ")
# • Nome: mais de 3 caracteres
if len(nome) <= 3:
    print("Nome com menos de 3 caracteres!!!")
    exit()
idade = int(input("Digite sua idade: "))
# • Idade: entre 0 e 150;
if idade < 0 or idade > 150:
    print("Idade fora da faixa 0 - 150!!!")
    exit()
salario = float(input("Digite seu salário: "))
# • Salário: maior que zero;
if salario <= 0:
    print("Salario menor que 0!!!")
    exit()
sexo = input("Digite seu sexo (f/m): ")
sexo = sexo.upper()
# • Sexo: 'f' ou 'm';
if sexo not in ("F", "M"):
    print("Sexo inválido!!!")
    exit()
estado_civil = input("Digite seu estado civil (s, c, v, d): ")
estado_civil = estado_civil.upper()
# • Estado civil: 's', 'c', 'v' ou 'd'.
if estado_civil not in ("C", "S", "V", "D"):
    print("Estado civil inválido!!!")


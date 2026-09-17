# Exercício 42 - Lista de Exercícios 03
faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
numero = float(input("Digite um número de 0 a 100: "))
while numero >= 0:
    if numero > 100:
        print("Número inválido!")
    elif numero <= 25:
        faixa1 = faixa1 + 1
    elif numero <= 50:
        faixa2 = faixa2 + 1
    elif numero <= 75:
        faixa3 = faixa3 + 1
    else:
        faixa4 = faixa4 + 1
    numero = float(input("Digite outro número ou um negativo para encerrar: "))
print("Valores entre 0 e 25:", faixa1)
print("Valores maiores que 25 até 50:", faixa2)
print("Valores maiores que 50 até 75:", faixa3)
print("Valores maiores que 75 até 100:", faixa4)

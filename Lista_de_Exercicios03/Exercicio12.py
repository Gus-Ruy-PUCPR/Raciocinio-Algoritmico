# Exercício 12 - Lista de Exercícios 03

numero = int(input("Digite um número de 1 a 10: "))
while numero < 1 or numero > 10:
    print("Número inválido!")
    numero = int(input("Digite um número de 1 a 10: "))
for contador in range(1, 11):
    resultado = numero * contador
    print(numero, "X", contador, "=", resultado)
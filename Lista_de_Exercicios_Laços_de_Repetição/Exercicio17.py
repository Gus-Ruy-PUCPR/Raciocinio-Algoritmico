# Exercício 17 - Lista de Exercícios 03

numero = int(input("Digite um número: "))
while numero < 0:
    print("Não pode ser um número negativo!")
    numero = int(input("Digite outro número: "))
fatorial = 1
for contador in range(1, numero + 1):
    fatorial = fatorial * contador
print("O fatorial de", numero, "é", fatorial)
# Exercício 28 - Lista de Exercícios 03
quantidade = int(input("Quantos CDs existem na coleção? "))
while quantidade <= 0:
    print("Quantidade inválida!")
    quantidade = int(input("Digite novamente: "))
total = 0
for contador in range(quantidade):
    valor = float(input("Digite o valor pago no CD: R$ "))
    while valor < 0:
        print("Valor inválido!")
        valor = float(input("Digite novamente: R$ "))
    total = total + valor
media = total / quantidade
print(f"Valor total: R$ {total:.2f}")
print(f"Média por CD: R$ {media:.2f}")
# Exercício 41 - Lista de Exercícios 03
divida = float(input("Digite o valor da dívida: R$ "))
while divida < 0:
    print("Valor inválido!")
    divida = float(input("Digite novamente: R$ "))
print("Dívida | Juros | Parcelas | Valor da parcela")
for opcao in range(1, 6):
    if opcao == 1:
        parcelas = 1
        porcentagem = 0
    elif opcao == 2:
        parcelas = 3
        porcentagem = 0.10
    elif opcao == 3:
        parcelas = 6
        porcentagem = 0.15
    elif opcao == 4:
        parcelas = 9
        porcentagem = 0.20
    else:
        parcelas = 12
        porcentagem = 0.25
    juros = divida * porcentagem
    total = divida + juros
    valor_parcela = total / parcelas
    print(f"R$ {total:.2f} | R$ {juros:.2f} | {parcelas} | R$ {valor_parcela:.2f}")
# Exercício 31 — Caixa registradora. Sarah Gabrielli Rodrigues de Souza Ribeiro - 30/08/2026.
# Implementar uma caixa registradora rudimentar, com números desconhecidos de valores.
# O 0 é fim da compra. Mostrar o total, perguntar o valor em dinheiro (não pode ser menor que o total) e calcule o troco.
# Perguntar se haverá uma nova compra e encerrar quando dizer não.

while True: # REPETIÇÃO CONDICIONAL — quando o número de voltas é desconhecido

    Total = 0
    Produto = 1
    print("Bem-vindo à nossa lojinha!")
    while True:
        try: # SENTINELA — encerra leitura de quantidade desconhecida
            Valor = float(input('Por gentileza, digite o valor do produto ("0" para encerrar): '))
            if Valor < 0: 
                print("Valor inválido! Por favor, tente novamente.")
                continue

            print(Produto, "º Produto: R$", format(Valor, ".2f")) # SAÍDA — duas casas decimais

            if Valor == 0:
                break

            Total += Valor # ACUMULADOR — soma valores
            Produto += 1 # CONTADOR — conta ocorrências

        except ValueError:
            print("Valor inválido! Por gentileza, tente novamente.")
            continue

    print("Total: R$", format(Total, ".2f"))

    while True:
        try:
            Pagamento = float(input("Insira a quantidade de dinheiro para realizar o pagamento: R$ "))
            
            if Pagamento < Total: # MÁXIMO / MÍNIMO — o primeiro valor inicializa a comparação
                print("O valor não é o suficiente! Digite um valor mais alto.")
                continue
            # GERAÇÃO DE SÉRIE — o próximo termo depende dos anteriores
            Troco = Pagamento - Total # SUBTRAÇÃO — diminui valores
            
            print("Este é o valor do seu troco: R$", format(Troco, ".2f"))
            break

        except ValueError:
            print("Valor inválido! Por gentileza, tente novamente.")

    NovaCompra = input('Gostaria de realizar uma nova compra? Se sim, digite "Sim", se deseja encerrar, digite "Não": ')
    # SENTINELA — encerra leitura de quantidade desconhecida
    if NovaCompra == "Não" or NovaCompra == "não":
        break
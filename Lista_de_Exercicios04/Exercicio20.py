# Exercício 20 — Enquete sobre sistemas operacionais de servidor
# Nível 4 — Avançado · Padrão algorítmico: Entrada indeterminada e lista de contadores
# Elabore um programa que receba votos para escolher o melhor sistema operacional
# para uso em servidores.
# As opções válidas são de 1 a 6 e o valor 0 encerra a votação.
# Valores fora da faixa devem ser rejeitados.
# Ao final, mostre os votos e percentuais de cada opção, o total de votos
# e o sistema operacional mais votado.

# Cria uma lista com o nome de cada sistema operacional.
sistemas = ["", "Windows Server", "Red Hat Enterprise Linux",
            "Ubuntu Server", "Debian", "FreeBSD", "Outro"]

# Cria uma posição para cada opção e começa todos os votos em zero.
votos = [0, 0, 0, 0, 0, 0, 0]

# Começa o total de votos com zero.
total = 0

# Pede uma opção ao usuário. O número 0 encerra a votação.
opcao = int(input("Digite seu voto (1 a 6 ou 0 para encerrar): "))

# Continua recebendo votos enquanto o usuário não digitar zero.
while opcao != 0:

    # Verifica se a opção digitada está entre 1 e 6.
    if opcao >= 1 and opcao <= 6:
        # Acrescenta 1 voto à opção escolhida.
        votos[opcao] = votos[opcao] + 1
        # Acrescenta 1 ao total de votos válidos.
        total = total + 1
    # Se a opção não estiver entre 1 e 6, executa o bloco abaixo.
    else:
        # Avisa que a opção digitada é inválida.
        print("Opção inválida!")
    # Pede o próximo voto antes de repetir o while.
    opcao = int(input("Digite seu voto (1 a 6 ou 0 para encerrar): "))
# Mostra o cabeçalho do resultado da enquete.
print("Sistema Operacional - Votos - %")
# Só calcula o resultado se existir pelo menos um voto.
if total > 0:
    # Considera inicialmente a opção 1 como vencedora.
    vencedor = 1
    # Guarda os votos da opção 1 para começar a comparação.
    maior_votos = votos[1]
    # Percorre as opções de 1 até 6.
    for i in range(1, 7):
        # Calcula o percentual de votos da opção atual.
        percentual = votos[i] * 100 / total
        # Mostra o sistema, a quantidade de votos e o percentual.
        print(sistemas[i], "-", votos[i], "-", percentual, "%")
        # Verifica se a opção atual recebeu mais votos que a vencedora.
        if votos[i] > maior_votos:
            # Atualiza a maior quantidade de votos encontrada.
            maior_votos = votos[i]
            # Guarda o número da nova opção vencedora.
            vencedor = i
    # Calcula o percentual de votos do sistema vencedor.
    percentual_vencedor = maior_votos * 100 / total
    # Mostra o total de votos válidos.
    print("Total:", total)
    # Mostra o nome do sistema operacional mais votado.
    print("O Sistema Operacional mais votado foi", sistemas[vencedor])
    # Mostra a quantidade de votos do vencedor.
    print("Votos:", maior_votos)
    # Mostra o percentual de votos do vencedor.
    print("Percentual:", percentual_vencedor, "%")
# Se não existir nenhum voto, executa o bloco abaixo.
else:
    # Informa que nenhum voto foi computado.
    print("Nenhum voto foi computado.")
    
# Exercício 20 - Fim
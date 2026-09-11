# Exercício 19 — Enquete do melhor jogador
# Nível 4 — Avançado · Padrão algorítmico: Entrada indeterminada e lista de contadores
# Elabore um programa que receba votos para jogadores numerados de 1 a 23.
# O valor 0 deve encerrar a votação e valores inválidos devem ser ignorados.
# Ao final, mostre o total de votos, os jogadores que receberam votos,
# a quantidade e o percentual de votos de cada jogador.
# Informe também qual jogador foi escolhido como o melhor da partida.

# Cria uma lista vazia para guardar os votos.
votos = []

# Repete 24 vezes para criar as posições de 0 até 23.
for i in range(24):
    # Adiciona zero em cada posição, pois ninguém recebeu votos ainda.
    votos.append(0)

# Começa o total de votos com zero.
total = 0

# Pede o número do jogador. O número 0 encerra a votação.
jogador = int(input("Número do jogador (0 para encerrar): "))

# Continua recebendo votos enquanto o usuário não digitar zero.
while jogador != 0:

    # Verifica se o jogador está entre 1 e 23.
    if jogador >= 1 and jogador <= 23:
        # Acrescenta 1 voto ao jogador escolhido.
        votos[jogador] = votos[jogador] + 1
        # Acrescenta 1 ao total de votos válidos.
        total = total + 1
    # Se o número não estiver entre 1 e 23, executa o bloco abaixo.
    else:
        # Avisa que o número digitado é inválido.
        print("Número inválido!")
    # Pede o próximo voto antes de repetir o while.
    jogador = int(input("Número do jogador (0 para encerrar): "))
# Mostra o título do resultado.
print("Resultado da votação:")
# Mostra a quantidade total de votos válidos.
print("Foram computados", total, "votos.")
# Só calcula o resultado se existir pelo menos um voto.
if total > 0:
    # Considera inicialmente o jogador 1 como o melhor.
    melhor = 1
    # Guarda a quantidade de votos do jogador 1 para começar a comparação.
    maior_votos = votos[1]
    # Percorre os jogadores de 1 até 23.
    for i in range(1, 24):
        # Verifica se o jogador recebeu pelo menos um voto.
        if votos[i] > 0:
            # Calcula o percentual de votos desse jogador.
            percentual = votos[i] * 100 / total
            # Mostra o número, os votos e o percentual do jogador.
            print("Jogador", i, "-", votos[i], "votos -", percentual, "%")
        # Verifica se esse jogador recebeu mais votos que o melhor atual.
        if votos[i] > maior_votos:
            # Atualiza a maior quantidade de votos encontrada.
            maior_votos = votos[i]
            # Guarda o número do novo melhor jogador.
            melhor = i
    # Calcula o percentual de votos do jogador vencedor.
    percentual_melhor = maior_votos * 100 / total
    # Mostra o número do melhor jogador.
    print("O melhor jogador foi o número", melhor)
    # Mostra quantos votos o melhor jogador recebeu.
    print("Votos:", maior_votos)
    # Mostra o percentual de votos do melhor jogador.
    print("Percentual:", percentual_melhor, "%")
# Se não existir nenhum voto, executa o bloco abaixo.
else:
    # Informa que nenhum voto foi computado.
    print("Nenhum voto foi computado.")

# Exercício 19 - Fim
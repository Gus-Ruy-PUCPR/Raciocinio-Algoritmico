# Exercício 24 — Uso de espaço em disco pelos usuários
# Nível 4 — Avançado · Padrão algorítmico: Listas paralelas e relatório formatado
# A partir das listas de usuários e dos espaços ocupados em bytes,
# calcule o espaço utilizado por cada usuário em megabytes e seu percentual de uso.
# Considere 1 MB igual a 1.048.576 bytes.
# Ao final, mostre também o espaço total e o espaço médio ocupados,
# utilizando vírgula como separador decimal.

# Cria uma lista com os nomes dos usuários.
usuarios = ["alexandre", "anderson", "antonio",
            "carlos", "cesar", "rosemary"]
# Cria outra lista com o espaço usado por cada usuário em bytes.
espacos = [456123789, 1245698456, 123456456,
           91257581, 987458, 789456125]
# Começa o espaço total com zero.
total = 0
# Percorre todas as posições da lista de espaços.
for i in range(len(espacos)):
    # Soma o espaço de cada usuário ao total.
    total = total + espacos[i]
# Mostra o título do relatório.
print("ACME Inc. Uso do espaço em disco pelos usuários")
# Mostra uma linha para separar as partes do relatório.
print("--------------------------------------------------------------")
# Mostra o cabeçalho das informações.
print("Nr. Usuário - Espaço utilizado - % do uso")
# Percorre todos os usuários da lista.
for i in range(len(usuarios)):
    # Converte o espaço de bytes para megabytes.
    espaco_mb = espacos[i] / 1048576
    # Calcula o percentual do espaço total usado pelo usuário.
    percentual = espacos[i] * 100 / total
    # Deixa o espaço com duas casas decimais e troca ponto por vírgula.
    espaco_texto = ("%.2f" % espaco_mb).replace(".", ",")
    # Faz a mesma formatação com o percentual.
    percentual_texto = ("%.2f" % percentual).replace(".", ",")
    # Mostra o número, o usuário, o espaço usado e o percentual.
    print(i + 1, usuarios[i], "-", espaco_texto, "MB -", percentual_texto + "%")
# Converte o espaço total de bytes para megabytes.
total_mb = total / 1048576
# Divide o total pela quantidade de usuários para calcular a média.
media_mb = total_mb / len(usuarios)
# Formata o total com duas casas decimais e vírgula.
total_texto = ("%.2f" % total_mb).replace(".", ",")
# Formata a média com duas casas decimais e vírgula.
media_texto = ("%.2f" % media_mb).replace(".", ",")
# Mostra outra linha para separar o final do relatório.
print("--------------------------------------------------------------")
# Mostra o espaço total ocupado.
print("Espaço total ocupado:", total_texto, "MB")
# Mostra o espaço médio ocupado por usuário.
print("Espaço médio ocupado:", media_texto, "MB")

# Exercício 24 - Fim
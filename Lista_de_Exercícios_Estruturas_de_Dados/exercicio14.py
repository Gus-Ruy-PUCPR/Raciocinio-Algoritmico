# Exercício 14 — Termos mais citados nas avaliações do app. Sarah Gabrielli Rodrigues de Souza Ribeiro. 18 - 09 - 2026.
# Percorrer os comentários, eliminar pontuação, converter para minúsculo, descarte as palavras da lista de exclusão e conte a frequência de cada termo. 
# Exibir ordenado por frequência decrescente e, em empate, ordem alfabética
# Requisitos técnicos:
# ● Aplicar o padrão de acumulação com get(palavra, 0) + 1.
# ● Separar as palavras com split().
# ● Ordenar com sorted() e chave composta.

CIANO = "\033[36m" 
RESET = "\033[0m"
import string

Comentarios = {
    1: "O aplicativo é prático, e um sistema rápido!",
    2: "O aplicativo é prático, bonito, mas limitado, depois de um tempo fica em desuso.",
    3: "Bonito, mas trava demais! Apenas pra acessar o menu, demorou 1h!! Melhorem.",
    4: "Rápido e bonito."
}

Exclusão = {"o", "a", "e", "é", "pra", "mas", "porém", "demais", "uma", "possui",
             "um", "depois", "de", "fica", "em", "1h","acessar", "apenas" }

Frequencia = {}

for Comentario in Comentarios.values():

    Comentario = Comentario.lower()

    Comentario = Comentario.translate(
        str.maketrans("", "", string.punctuation)
    )

    Palavras = Comentario.split()

    for Palavra in Palavras:

        if Palavra not in Exclusão:

            Frequencia[Palavra] = Frequencia.get(Palavra, 0) + 1

Ordenado = sorted(
    Frequencia.items(),
    key=lambda item: (-item[1], item[0])
)

print(f"{CIANO} Estes se tratam dos termos mais citados: {RESET}")

for Palavra, Quantidade in Ordenado:
    print(f"● {Palavra}: {CIANO}{Quantidade}{RESET}")

# FIM - Exercício 14
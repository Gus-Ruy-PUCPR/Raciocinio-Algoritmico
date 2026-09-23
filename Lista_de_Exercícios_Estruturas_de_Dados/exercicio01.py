# Exercício 1 — Estações de metrô. Sarah Gabrielli Rodrigues de Souza Ribeiro. 11 - 09 - 2026.
# Crie uma lista de tuplas em que cada tupla represente uma estação com nome, linha, latitude e longitude. Percorra a lista com desempacotamento e exiba um relatório alinhado em colunas, informando ao final o total de estações.

from collections import namedtuple
CIANO = "\033[36m" 
RESET = "\033[0m"


Estação = namedtuple ("Estação", ["Nome", "Linha", "Latitude", "Longitude"], ) # Permite citar o elemto sem precisar do índice
Estações = []

while True:
    Nome = input ("Por gentileza, me diga o nome da estação: ")
    Linha = input ("Por gentileza, me diga a linha: ")
    Latitude = float(input("Por gentileza, me diga a Latitude: "))
    Longitude = float(input("Por gentileza, me diga a longitude: "))
    NovaEstação = Estação (Nome, Linha, Latitude, Longitude,) # Criando uma tupla por ser informações que não devem ser alteradas.
    Estações.append (NovaEstação) # Adicionando uma tupla com lista a uma outra lista, para poder alterar certas informações dentro da lista na tupla.
    if input ("Gostaria de adicionar mais uma estção? [S/N]: ").strip().upper() == "N":
        break
print(f"{CIANO}{'Nome':<20}{'Linha':<10}{'Latitude':<15}{'Longitude':<15}{RESET}")
print(f"{CIANO}-{RESET}" * 60)

for Nome, Linha, Latitude, Longitude in Estações:

    print(f"{Nome:<20}{Linha:<10}{Latitude:<15.4f}{Longitude:<15.4f}")

print(f"Total de estações presentes: {len(Estações)}")

# FIM - Exercício 01
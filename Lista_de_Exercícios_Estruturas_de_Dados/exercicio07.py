# Exercício 7 — Pontos turísticos com campos nomeados
# Contexto. Um aplicativo de turismo registra pontos históricos com coordenadas. Acessar ponto[3] tornou o código
# ilegível e propenso a erro de índice.
# Tarefa. Use namedtuple para criar o tipo Ponto com os campos nome, cidade, país, latitude e longitude. Cadastre
# três pontos, exiba-os por nome de campo e demonstre os métodos _asdict() e _replace().
# Requisitos técnicos:
# ● Importar namedtuple de collections
# ● Acessar por índice e por nome
# ● Mostrar que _replace() não altera o original

from collections import namedtuple

# Tupla nomeada
PontosTuristicos = namedtuple("PontoTuristico", ["nome","cidade", "pais", "latitude", "longitude"])

# TUplas pre-cadastradas
ponto1 = PontosTuristicos("Jardim Botanico", "Curitiba", "Brasil", "5000", "5000")
ponto2 = PontosTuristicos("Cristo Redentor", "Rio de Janeiro", "Brasil", "2600", "2200")
ponto3 = PontosTuristicos("Palácio do Planalto", "Brasília", "Brasil", "5000", "5000")

# Exibição por nome de campo
print("\n"*2 + "\n" + "-"*50)
print(f"Ponto turistico: {ponto1.nome}\nCidade: {ponto1.cidade}\nPaís:{ponto1.pais}\nLatitude: {ponto1.latitude}\nLongitude: {ponto1.longitude}" + "\n" + "-"*50)
print(f"Ponto turistico: {ponto2.nome}\nCidade: {ponto2.cidade}\nPaís:{ponto2.pais}\nLatitude: {ponto2.latitude}\nLongitude: {ponto2.longitude}" + "\n" + "-"*50)
print(f"Ponto turistico: {ponto3.nome}\nCidade: {ponto3.cidade}\nPaís:{ponto3.pais}\nLatitude: {ponto3.latitude}\nLongitude: {ponto3.longitude}" + "\n" + "-"*50)
print("\n")

# Método _asdict()
print("-"*50)
print(ponto1._asdict())
print("-"*50)
print(ponto2._asdict())
print("-"*50)
print(ponto3._asdict())
print("-"*50)
print("\n")

# Método _replace()
ponto1 = ponto1._replace(nome="Jardim Municipal")
print("-"*50)
print(ponto1)
print("-"*50)
ponto2 = ponto2._replace(nome="Pão de Açucar")
print(ponto2)
print("-"*50)
ponto3 = ponto3._replace(nome="Palácio da Alvorada")
print(ponto3)
print("-"*50)
print("\n"*2)

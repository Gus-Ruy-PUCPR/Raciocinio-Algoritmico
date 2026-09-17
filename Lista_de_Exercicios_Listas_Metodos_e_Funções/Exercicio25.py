# Exercício 25 - Thiago Augusto da Silva - 02/09
# Elabore um programa que simule o lançamento de um dado de seis faces. Lance o dado 100 vezes, armazene
# os resultados em uma lista e mostre, ao final, quantas vezes cada face foi obtida, com o percentual
# correspondente e um histograma feito com asteriscos.
# Use uma lista de contadores para as faces de 1 a 6 e a função random.randint para simular os lançamentos.

import random # Este é o único exercício da lista em que se autoriza a importação de uma biblioteca.

rolagem = int(0)
resultados = []
visual = str("*") # Esta string servirá para criação do histograma no final

# Contadores que contam quantas vezes um número foi observado nos resultados
vezes1 = int(0)
vezes2 = int(0)
vezes3 = int(0)
vezes4 = int(0)
vezes5 = int(0)
vezes6 = int(0)

for i in range(100):
    rolagem = random.randint(1, 6)
    resultados.append(rolagem)

# Dentro das restrições da lista de exercício, não podemos fazer a varredura automática com count, então vamos contar os resultados manualmente
for i in range(len(resultados)):
    if resultados[i] == 1:
        vezes1 += 1
    elif resultados[i] == 2:
        vezes2 += 1
    elif resultados[i] == 3:
        vezes3 += 1
    elif resultados[i] == 4:
        vezes4 += 1
    elif resultados[i] == 5:
        vezes5 += 1
    else: vezes6 += 1

print("Resultado de 100 lançamentos:\n\nFace | Ocorrências | Percentual | Histograma")
print(f"1    |      {vezes1}     |   {vezes1:.02f}%   | {visual * vezes1}")
print(f"2    |      {vezes2}     |   {vezes2:.02f}%   | {visual * vezes2}")
print(f"3    |      {vezes3}     |   {vezes3:.02f}%   | {visual * vezes3}")
print(f"4    |      {vezes4}     |   {vezes4:.02f}%   | {visual * vezes4}")
print(f"5    |      {vezes5}     |   {vezes5:.02f}%   | {visual * vezes5}")
print(f"6    |      {vezes6}     |   {vezes6:.02f}%   | {visual * vezes6}")

# Exercício 25 - Fim
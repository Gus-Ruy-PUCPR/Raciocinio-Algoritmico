# Exercicio 2 — Leitura de sensor e trilha de auditoria. Sarah Gabrielli Rodrigues de Souza Ribeiro. 16 - 09 - 2026.
# Cada leitura precisa ficar registrada exatamente como foi coletada: correções geram uma nova versão, jamais alteram a original.
# Represente uma leitura como tupla (identificador, data-hora, valor). Alterar o valor medido e trate o erro. Produza versão corrigida como tupla. 
# Mostrar os identificadores de objeto (id) das duas versões e comprove que são objetos distintos.
CIANO = "\033[36m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

Identificador = input("Por gentileza, digite o identificador do sensor: ")
DataHora = input("Por gentileza, digite a data e a hora da leitura do sensor: ")
Valor = float(input("Por gentileza, digite o valor medido pelo sensor: "))

Leitura1 = (Identificador, DataHora, Valor,)

print(f"Esta é a leitura original realizada pelo sensor: {CIANO}{Leitura1}{RESET}")

Correção = float(input("Por favor, me insira o valor corrigido da leitura realizada pelo sensor: "))

try:
    Leitura1[2] = Correção

except TypeError as erro:
    print(f"{CIANO} Atenção! A primeira leitura do sensor não pode ser alterada.{RESET}")
    print(f"Este é o erro gerado: {VERMELHO}{erro}{RESET}")

LeituraCorrigida = (Leitura1[0], Leitura1[1], Correção,)

print(f"Esta é a primeira leitura informada: {MAGENTA}{Leitura1}{RESET}")
print(f"Esta se trata da leitura corrigida: {VERDE}{LeituraCorrigida}{RESET}")

print(f"O ID da primeira leitura é: {CIANO}{id(Leitura1)}{RESET}")
print(f"O ID da leitura corrigida é: {CIANO}{id(LeituraCorrigida)}{RESET}")

print(f"Se tratam da mesma coisa? {VERMELHO}{Leitura1 is LeituraCorrigida}{RESET}") 

# FIM - Exercício 02
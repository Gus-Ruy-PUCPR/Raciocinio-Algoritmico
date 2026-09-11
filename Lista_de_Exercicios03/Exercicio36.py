# Exercício 36 - Lista de Exercícios 03
# Leitura do número da tabuada
numero = int(input("Montar a tabuada de: "))

# Leitura do limite inicial e final
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

# Validação: o valor final não pode ser menor que o inicial
while fim < inicio:
    print("Erro: O valor final não pode ser menor que o valor inicial!")
    fim = int(input("Terminar em: "))

print(f"\nVou montar a tabuada de {numero} começando em {inicio} e terminando em {fim}:")

# Gera a tabuada no intervalo definido
for i in range(inicio, fim + 1):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")
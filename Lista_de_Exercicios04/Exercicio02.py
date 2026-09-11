# Exercício 02 — Exibição na ordem inversa. Sarah Gabrielli Rodrigues de Souza Ribeiro - 07/09/2026.
# Ler uma lista com 10 números reais, mostrar na ordem inversa da digitação e com duas casas decimais.
Numeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(10):
    Num = float(input("Por gentileza, digite um número: "))
    Numeros[i] = Num

print("Estes são os números que compõem a lista na ordem inversa:")

for i in range(9, -1, -1):
    print(f"• {Numeros[i]: .2f}", end = " ")
    
# Exercício 02 - FIM.
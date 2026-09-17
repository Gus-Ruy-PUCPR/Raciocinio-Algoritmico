limite_servico = 50
multa = 4

r = ""
lista_peixes = []
peso_peixes = 0
tarifa_a_pagar = 0
i = 0

while r != "s":
    lista_peixes.append(float(input(f"Qual o peso do peixe {i+1} ou o total de peso dos peixes? ")))
    r = input("Deseja progredir com o calculo da tarifa? (s/n) ")

for i in range(len(lista_peixes)):
    peso_peixes += lista_peixes[i]

if peso_peixes > 50:
    tarifa_a_pagar = (peso_peixes - 50)*multa
    print(f"Tarifa a pagar é: {tarifa_a_pagar}")
    print(f"Peso total dos peixes é {peso_peixes}")

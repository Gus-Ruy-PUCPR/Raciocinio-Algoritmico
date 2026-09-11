# Exercício 21 - Thiago Augusto da Silva - 01/09
# As Organizações Tabajara decidiram conceder um abono aos seus colaboradores em reconhecimento ao
# resultado alcançado no ano. Você foi contratado para desenvolver a aplicação que projeta o gasto com esse
# pagamento. A regra acordada é a seguinte: cada colaborador recebe o equivalente a 20% do seu salário bruto
# de dezembro, respeitado o piso de R$ 600,00 — ou seja, quem tiver salário muito baixo recebe esse valor
# mínimo.
# Não há, neste momento, qualquer preocupação com tempo de casa, descontos ou impostos. O programa
# deve permitir a digitação de um número indeterminado de salários, encerrando quando for informado o
# valor 0. Ao final, deve apresentar:
# a) o salário de cada colaborador, junto com o valor do abono;
# b) o número total de colaboradores processados;
# c) o valor total a ser gasto com o pagamento dos abonos;
# d) o número de colaboradores que receberão o valor mínimo
# e) o maior valor pago como abono.

salariosLista = []
abonosLista = []
abonoMaior = float(0.0)
abonosTotal = float(0.0)
colaboradores = int(0)
colaboradoresMin = int(0)

while True:
    try:
        salario = float(input("Digite o valor do seu salário (Ou digite 0 para encerrar): "))
    except:
        print("Por favor insira um valor válido!")
    if salario == 0:
        break
    salariosLista.append(salario)
    abono = salario * 0.20
    if abono < 600.00: # Se valor for menor que minimo, o abono é forçado a ser o minímo e contamos quantas vezes tivemos que fazer isto
        abono = 600
        colaboradoresMin += 1
    abonosLista.append(abono)
    colaboradores += 1
    if abono > abonoMaior: abonoMaior = abono
    abonosTotal += abono

print("Salário | Abono")
for i in range(colaboradores):
    print(f"RS$ {salariosLista[i]:.2f} | R$ {abonosLista[i]:.2f}")
print(f"Foram processados: {colaboradores} colaboradores\nTotal gasto com abonos: R$ {abonosTotal:.2f}")
print(f"Valor mínimo pago à {colaboradoresMin} colaboradores\nMaior valor de abono pago: R$ {abonoMaior:.2f}")

# Exercício 21 - Fim
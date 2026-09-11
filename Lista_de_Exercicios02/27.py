# 27. Validação de data
# Faça um programa que peça uma data no formato dd/mm/aaaa e determine se ela é uma data válida,
# considerando a quantidade de dias de cada mês e a ocorrência de anos bissextos. O programa deve rejeitar
# entradas mal formatadas, como 1/2/2026 ou 31-12-2026.
# Dica: a entrada é lida como texto. Use as fatias data[0:2], data[3:5] e data[6:10] para separar dia, mês e ano,
# e o método .isdigit() para verificar se cada parte contém apenas dígitos antes de convertê-las com int().
# data = input("Digite a data no formato dd/mm/aaaa: ")

data = input("Digite a data no formato dd/mm/aaaa: ")

if len(data) != 10 or data[2] != "/" or data[5] != "/":
    print("Erro: A data deve estar estritamente no formato dd/mm/aaaa.")
else:
    parte_dia = data[0:2]
    parte_mes = data[3:5]
    parte_ano = data[6:10]

    if not (parte_dia.isdigit() and parte_mes.isdigit() and parte_ano.isdigit()):
        print("Erro: Dia, mês e ano devem conter apenas números.")
    else:
        dia = int(parte_dia)
        mes = int(parte_mes)
        ano = int(parte_ano)

        if ano < 1:
            print("Erro: Ano inválido.")
        else:
            bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

            if mes < 1 or mes > 12:
                print("Erro: O mês deve estar entre 01 e 12.")
            else:
                if mes == 2:
                    if bissexto:
                        dias_no_mes = 29
                    else:
                        dias_no_mes = 28
                elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                    dias_no_mes = 30
                else:
                    dias_no_mes = 31

                if dia < 1 or dia > dias_no_mes:
                    print(f"Erro: O dia {dia} é inválido para o mês informado.")
                else:
                    print(f"A data {data} é VÁLIDA.")
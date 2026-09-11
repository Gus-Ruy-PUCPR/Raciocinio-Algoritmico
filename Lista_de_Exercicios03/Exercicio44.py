#                           Exercício 44 - Thiago Augusto da Silva - 31/08                                          #
#####################################################################################################################
# Em uma eleição presidencial existem quatro candidatos: 1 – Ana, 2 – Bruno, 3 – Carla, 4 – Diego. Além disso, o    #
# código 5 representa voto nulo e o código 6, voto em branco. O valor 0 encerra a votação.                          #
# Faça um programa que calcule e mostre: o total de votos de cada candidato; o total de nulos; o total de brancos;  #
# o percentual de nulos e o percentual de brancos sobre o total de votos.                                           #
# Códigos inválidos devem ser desconsiderados com aviso, e o programa deve tratar o caso de nenhum voto             #
# registrado.                                                                                                       #
#####################################################################################################################

codigo = int(1) # Esta variavel comanda quando o programa acaba assim como o candidato votado
votosTotal = int(0) # O resto das variaveis sao criadas como 0 para evitar erros e podermos contar os votos depois
votosAna = int(0)
votosBruno = int(0)
votosCarla = int(0)
votosDiego = int(0)
votosNulo = int(0)
votosBranco = int(0)

while codigo != 0:
    try:
        print("Códigos dos candidatos: \n 1 - Ana \n 2 - Bruno\n 3 - Carla\n 4 - Diego\n 5 - Voto nulo\n 6 - Voto em branco")
        codigo = int(input("Digite o código do seu candidato ou digite zero para encerrar o programa\n"))
    except:
        print("Tente novamente com um código válido!")
    if codigo not in (0, 1, 2, 3, 4, 5, 6):
        print("Tente novamente com um código válido!")
    votosTotal += 1
    if codigo == 1:
        votosAna += 1
    elif codigo == 2:
        votosBruno += 1
    elif codigo == 3:
        votosCarla += 1
    elif codigo == 4:
        votosDiego += 1
    elif codigo == 5:
        votosNulo += 1
    elif codigo == 6:
        votosBranco += 1
if votosTotal == 0:
    print("Não houve nenhum voto!")
    exit()
porcentagemBrancos = votosBranco / votosTotal
porcentagemNulo = votosNulo / votosTotal
print("\n O total de votos foram ", votosTotal)
print("\n", votosAna, " Votos para Ana\n", votosBruno, " Votos para Bruno\n", votosCarla, " Votos para Carla\n", votosDiego, " Votos para Diego")
print("Do total, %.2f" %porcentagemBrancos, "% ", "dos votos foram Brancos e %.2f" %porcentagemNulo, "%", "dos votos foram Nulos")
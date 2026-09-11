# 28. Monitoramento de sala de servidores
# Uma sala de servidores do campus é monitorada por um sistema ciberfísico que coleta, a cada minuto, a
# temperatura interna (°C), a umidade relativa do ar (%) e o estado do nobreak (OK ou FALHA). Faça um
# programa que leia esses três valores e classifique a situação em um dos quatro níveis abaixo, imprimindo o
# nível e a ação recomendada:
# • EMERGÊNCIA — sempre que o nobreak estiver em FALHA, independentemente das demais leituras. Ação:
# acionar a equipe de plantão imediatamente.
# • CRÍTICO — nobreak em OK, mas temperatura acima de 32 °C ou umidade acima de 80%. Ação: abrir
# chamado de prioridade alta.
# • ATENÇÃO — nobreak em OK, temperatura de 27 °C a 32 °C ou umidade de 65% a 80%. Ação: registrar
# ocorrência e monitorar.
# • NORMAL — nenhuma das condições anteriores. Ação: nenhuma.
# O programa deve rejeitar leituras fisicamente impossíveis: temperatura fora do intervalo de -20 °C a 80 °C,
# umidade fora do intervalo de 0% a 100%, ou estado do nobreak diferente de OK e FALHA.

temperatura = float(input("Digite a temperatura interna (°C): "))
umidade = float(input("Digite a umidade relativa do ar (%): "))
nobreak = input("Digite o estado do nobreak (OK ou FALHA): ").strip().upper()

if temperatura < -20 or temperatura > 80:
    print("Erro: Temperatura fisicamente impossível (deve estar entre -20 °C e 80 °C).")
elif umidade < 0 or umidade > 100:
    print("Erro: Umidade fisicamente impossível (deve estar entre 0% e 100%).")
elif nobreak != "OK" and nobreak != "FALHA":
    print("Erro: Estado do nobreak inválido (deve ser OK ou FALHA).")
else:
    if nobreak == "FALHA":
        print("\nSituação: EMERGÊNCIA")
        print("Ação recomendada: acionar a equipe de plantão imediatamente.")
    elif temperatura > 32 or umidade > 80:
        print("\nSituação: CRÍTICO")
        print("Ação recomendada: abrir chamado de prioridade alta.")
    elif (27 <= temperatura <= 32) or (65 <= umidade <= 80):
        print("\nSituação: ATENÇÃO")
        print("Ação recomendada: registrar ocorrência e monitorar.")
    else:
        print("\nSituação: NORMAL")
        print("Ação recomendada: nenhuma.")
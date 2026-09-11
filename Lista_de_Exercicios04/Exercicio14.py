# Exercício 14 — Temperaturas médias mensais
# Nível 3 — Intermediário · Padrão algorítmico: Listas paralelas, média e comparação
# Elabore um programa que receba a temperatura média de cada mês do ano
# e armazene os valores em uma lista.
# Calcule a média anual e mostre todas as temperaturas acima dessa média,
# indicando o mês correspondente por extenso.
# Caso nenhum mês fique acima da média, informe isso ao usuário.

# Cria uma lista com os nomes dos 12 meses.
meses = ["Janeiro", "Fevereiro", "Março", "Abril",
         "Maio", "Junho", "Julho", "Agosto",
         "Setembro", "Outubro", "Novembro", "Dezembro"]
# Cria uma lista vazia para guardar as temperaturas.
temperaturas = []
# Começa a soma das temperaturas com zero.
soma = 0
# Repete o bloco abaixo para os 12 meses do ano.
for i in range(12):
    # Pede a temperatura do mês atual e aceita número com casas decimais.
    temperatura = float(input("Digite a temperatura média de " + meses[i] + ": "))
    # Guarda a temperatura digitada na lista.
    temperaturas.append(temperatura)
    # Acrescenta a temperatura à soma.
    soma = soma + temperatura
# Divide a soma por 12 para calcular a média anual.
media = soma / 12
# Mostra a média anual das temperaturas.
print("Média anual:", media)
# Cria um contador para os meses que ficaram acima da média.
acima = 0
# Percorre as temperaturas dos 12 meses.
for i in range(12):
    # Verifica se a temperatura do mês é maior que a média anual.
    if temperaturas[i] > media:
        # Mostra o nome do mês e sua temperatura.
        print(meses[i], "-", temperaturas[i])
        # Acrescenta 1 ao contador de meses acima da média.
        acima = acima + 1
# Verifica se nenhum mês ficou acima da média.
if acima == 0:
    # Mostra uma mensagem quando o contador continua em zero.
    print("Nenhum mês ficou acima da média anual.")
    
# Exercício 14 - Fim
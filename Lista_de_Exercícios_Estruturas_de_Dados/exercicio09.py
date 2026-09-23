# Exercício 9 — Escala de plantão sem duplicidade. Sarah gabrielli Rodrigues de Souza Ribeiro. 16 - 09 - 26.
# Escala de plantão. Não pode haver dois plantonistas com o mesmo telefone, e um nome já cadastrado só é alterado com confirmação.
# Cadastro interativo em dicionário Nome → Telefone. Se o nome já existir, pergunte se deve atualizar; se o Telefone já pertencer a outro plantonista, recuse a inclusão. Ao final, mostre a escala e o total.
# 1. Testar a chave com in e o valor com in Agenda.values()
# 2. Normalizar a entrada com strip() e title()
# 3. Encerrar o laço com break.

Agenda = {}
CIANO = "\033[36m" 
RESET = "\033[0m"

print("Escala de plantão")
while True:
    Plantonista = input("Por gentileza, digite o nome do plantonista: ").strip().title()
    Telefone = input("Por gentileza, digite o Telefone do Plantonista: ").strip()

    if Plantonista in Agenda:
        if input(f"Atenção! Este plantonista já está cadastrado com o número {Agenda [Plantonista]}. Deseja alterá-lo? (S/N)").strip().upper() == "N":
            continue
    if Telefone in Agenda.values():
        print("Perdão, mas este telefone já está cadastrado para outro Plantonista!")
        continue
    Agenda [Plantonista] = Telefone

    if input("Gostaria de cadastrar um novo plantonista? (S/N): ").strip().upper() == "N":
                    break
    
print(f"{CIANO}{'Resultado da escala de plantão.':}{RESET}")
print(f"● {Agenda}")
print(f"{CIANO}{'Este é o total de plantonistas:'}{RESET} {len(Agenda)}")

# FIM - Exercício 09
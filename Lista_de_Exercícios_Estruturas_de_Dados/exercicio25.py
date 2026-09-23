# Exercício 25 — Desafio: fechamento do delivery. Sarah Gabrielli Rodrigues de Souza Ribeiro. 18 - 09 - 2026.
# Delivery fecha o caixa: total por pedido c/ taxa de entrega, faturamento, ticket médio, item mais vendido em unidades e item de maior receita.
# Lista tuplas (pedido, item, quantidade, preço unitário), três dicionários de acumulação — total por pedido, 
# quantidade por item e receita por item — relatório completo, participação percentual de cada item na receita.
# Requisitos técnicos:
# ● Três acumuladores no mesmo laço.
# ● Calcular ticket médio sobre o número de pedidos.
# ● Ordenar a curva de itens por receita decrescente.

CIANO = "\033[36m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

ItensVendidos = []

while True:

    Pedido = input('Por gentileza, digite o número do Pedido ("fim" para encerrar): ')

    if Pedido.lower() == "fim":
        break

    Item = input("Por gentileza, diga-me o nome do item: ")
    Quantidades = int(input("Por gentileza, diga-me a quantidade do item: "))
    PreçoUnitário = float(input("Por gentileza, diga-me o preço do item: "))
    ItensVendidos.append((Pedido, Item, Quantidades, PreçoUnitário))

TaxaEntrega = float(input("Por gentileza, diga-me o Valor da taxa de entrega: "))

TotalPorPedidos = {}
QuantidadesPorItens = {}
ReceitaPorItens = {}


for Pedido, Item, Quantidades, PreçoUnitário in ItensVendidos:

    SubTotal = Quantidades * PreçoUnitário

    TotalPorPedidos[Pedido] = (
        TotalPorPedidos.get(Pedido, 0.0) + SubTotal
    )

    QuantidadesPorItens[Item] = (
        QuantidadesPorItens.get(Item, 0) + Quantidades
    )

    ReceitaPorItens[Item] = (
        ReceitaPorItens.get(Item, 0.0) + SubTotal
    )


print(f"{MAGENTA}Este é o fechamento por pedido:{RESET}")

Faturamento = 0.0

for Pedido, Valor in TotalPorPedidos.items():

    TotalComEntrega = Valor + TaxaEntrega

    Faturamento += TotalComEntrega

    print(
        f"{Pedido}° R$ {Valor:.2f} + "
        f"R$ {TaxaEntrega:.2f} = "
        f"{CIANO}R$ {TotalComEntrega:.2f}{RESET}"
)


TicketMédio = Faturamento / len(TotalPorPedidos)


CampeãoQtd = ""
MaiorQtd = 0

for Item, Quantidades in QuantidadesPorItens.items():

    if Quantidades > MaiorQtd:
        MaiorQtd = Quantidades
        CampeãoQtd = Item


CampeãoReceita = ""
MaiorReceita = 0.0

for Item, receita in ReceitaPorItens.items():

    if receita > MaiorReceita:
        MaiorReceita = receita
        CampeãoReceita = Item


print(f"{MAGENTA}Este é o total de pedidos processados:{RESET} {len(TotalPorPedidos)}")
print(f"{MAGENTA}Este é o faturamento total:{RESET} R$ {Faturamento:.2f}")
print(f"{MAGENTA}Este é o Ticket médio:{RESET} R$ {TicketMédio:.2f}")
print(f"{MAGENTA}Este é o item mais vendido:{RESET} {CampeãoQtd} ({MaiorQtd} unidades)")
print(f"{MAGENTA}Este é o item de maior receita:{RESET} {CampeãoReceita} (R$ {MaiorReceita:.2f})")


print(f"{CIANO}Está é a curva de itens — Por receita: {RESET}")

for Item, receita in sorted(
    ReceitaPorItens.items(),
    key=lambda par: par[1],
    reverse=True
):

    Participação = receita / sum(ReceitaPorItens.values()) * 100

    print(
        f"{CIANO} ● {Item:<20} {RESET} "
        f"R$ {receita:>8.2f} "
        f"{MAGENTA}({Participação:>5.1f}%){RESET}"
    )
# FIM - Exercício 25
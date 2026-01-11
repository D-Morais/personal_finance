def calcular_totais(transacoes):
    renda = sum(t[2] for t in transacoes if t[4] == "renda")
    despesa = sum(t[2] for t in transacoes if t[4] == "despesa")
    return renda, despesa, renda - despesa

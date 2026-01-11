import streamlit as st
from repositorio.repositorio_financeiro import buscar_todas_transacoes
from core.servico_financeiro import calcular_totais
from core.statistics_service import to_dataframe, category_distribution
import matplotlib.pyplot as plt


def render_dashboard():
    st.title("📊 Dashboard Financeiro")

    dados = buscar_todas_transacoes()
    if not dados:
        st.warning("Nenhum dado cadastrado encontrado.")
        return
    renda, despesa, saldo = calcular_totais(dados)

    c1, c2, c3 = st.columns(3)
    c1.metric("Receitas", f"R$ {renda:.2f}")
    c2.metric("Despesas", f"R$ {despesa:.2f}")
    c3.metric("Saldo", f"R$ {saldo:.2f}")

    df = to_dataframe(dados)

    dist = category_distribution(df)

 #   fig, ax = plt.subplots()
 #   dist.plot(kind="bar", ax=ax)
 #   st.pyplot(fig)

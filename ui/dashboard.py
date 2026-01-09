import streamlit as st
from repositorio.repositorio_financeiro import fetch_all_transactions
from core.finance_service import calculate_totals
from core.statistics_service import to_dataframe, category_distribution
import matplotlib.pyplot as plt


def render_dashboard():
    st.title("📊 Dashboard Financeiro")

    data = fetch_all_transactions()
    income, expense, balance = calculate_totals(data)

    c1, c2, c3 = st.columns(3)
    c1.metric("Receitas", f"R$ {income:.2f}")
    c2.metric("Despesas", f"R$ {expense:.2f}")
    c3.metric("Saldo", f"R$ {balance:.2f}")

    df = to_dataframe(data)

    dist = category_distribution(df)

    fig, ax = plt.subplots()
    dist.plot(kind="bar", ax=ax)
    st.pyplot(fig)

import streamlit as st
import pandas as pd
import plotly.express as px


# Dados mockados apenas para layout
def load_mock_data():
    return pd.DataFrame({
        "Categoria": ["Alimentação", "Transporte", "Lazer", "Moradia"],
        "Valor": [1200, 450, 300, 1800]
    })


def render_dashboard():
    st.subheader("📊 Dashboard Financeiro")

    data = load_mock_data()

    total_despesas = data["Valor"].sum()
    saldo = 5000 - total_despesas

    # Cards principais
    col1, col2, col3 = st.columns(3)

    col1.metric("💼 Saldo Atual", f"R$ {saldo:,.2f}")
    col2.metric("📉 Total de Despesas", f"R$ {total_despesas:,.2f}")
    col3.metric("📈 Total de Receitas", "R$ 5.000,00")

    st.markdown("---")

    # Gráfico de gastos por categoria
    fig_pizza = px.pie(
        data,
        values="Valor",
        names="Categoria",
        title="Distribuição de Gastos por Categoria"
    )

    st.plotly_chart(fig_pizza, use_container_width=True)

    # Gráfico de barras
    fig_bar = px.bar(
        data,
        x="Categoria",
        y="Valor",
        title="Gastos por Categoria"
    )

    st.plotly_chart(fig_bar, use_container_width=True)

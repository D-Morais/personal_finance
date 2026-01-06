import streamlit as st
import pandas as pd
from datetime import date


# Dados mockados apenas para interface
def load_mock_history():
    return pd.DataFrame({
        "Data": ["2026-01-01", "2026-01-03", "2026-01-05", "2026-01-06"],
        "Descrição": ["Supermercado", "Uber", "Cinema", "Aluguel"],
        "Categoria": ["Alimentação", "Transporte", "Lazer", "Moradia"],
        "Tipo": ["Despesa", "Despesa", "Despesa", "Despesa"],
        "Valor (R$)": [320.50, 45.90, 60.00, 1800.00]
    })


def render_history():
    st.subheader("📜 Histórico de Transações")

    df = load_mock_history()

    # Filtros
    with st.expander("🔎 Filtros"):
        col1, col2, col3 = st.columns(3)

        with col1:
            tipo = st.selectbox("Tipo", ["Todos", "Despesa", "Receita"])

        with col2:
            categoria = st.selectbox(
                "Categoria",
                ["Todas"] + sorted(df["Categoria"].unique().tolist())
            )

        with col3:
            data_inicio, data_fim = st.date_input(
                "Período",
                value=(date(2026, 1, 1), date.today())
            )

    # Aplicação dos filtros (funcional e simples)
    filtered_df = df.copy()

    if tipo != "Todos":
        filtered_df = filtered_df[filtered_df["Tipo"] == tipo]

    if categoria != "Todas":
        filtered_df = filtered_df[filtered_df["Categoria"] == categoria]

    # Exibição da tabela
    st.dataframe(
        filtered_df,
        use_container_width=True
    )

    st.caption(f"Total de registros exibidos: {len(filtered_df)}")

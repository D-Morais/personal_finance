import streamlit as st
from datetime import date


def render_new_transaction():
    st.subheader("➕ Nova Transação")

    with st.form("new_transaction_form", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            valor = st.number_input(
                "Valor (R$)",
                min_value=0.0,
                step=0.01,
                format="%.2f"
            )

            tipo = st.selectbox(
                "Tipo",
                ["Despesa", "Receita"]
            )

        with col2:
            data = st.date_input(
                "Data",
                value=date.today()
            )

            categoria = st.selectbox(
                "Categoria",
                [
                    "Alimentação",
                    "Transporte",
                    "Moradia",
                    "Lazer",
                    "Educação",
                    "Outros"
                ]
            )

        descricao = st.text_input("Descrição")

        st.info("💡 A categoria será sugerida automaticamente em versões futuras.")

        submitted = st.form_submit_button("Salvar Transação")

        if submitted:
            st.success("Transação registrada com sucesso (simulação).")
import streamlit as st
from repositorio.repositorio_financeiro import insert_transaction


def render_new_transaction():
    st.title("➕ Nova Transação")

    desc = st.text_input("Descrição")
    amount = st.number_input("Valor", min_value=0.0)
    cat = st.text_input("Categoria")
    t_type = st.selectbox("Tipo", ["income", "expense"])
    date = st.date_input("Data")

    if st.button("Salvar"):
        insert_transaction(desc, amount, cat, t_type, date)
        st.success("Transação registrada!")

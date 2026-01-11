import streamlit as st
from repositorio.repositorio_financeiro import buscar_todas_transacoes


def render_historico():
    st.title("📜 Histórico")
    data = buscar_todas_transacoes()
    if not data:
        st.warning("Nenhum dado cadastrado encontrado.")
        return
    st.dataframe(data)

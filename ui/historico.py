import streamlit as st
from repositorio.repositorio_financeiro import fetch_all_transactions


def render_history():
    st.title("📜 Histórico")
    data = fetch_all_transactions()
    st.dataframe(data)

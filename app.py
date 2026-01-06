import streamlit as st
from ui.dashboard import render_dashboard
from ui.new_transaction import render_new_transaction
from ui.history import render_history

st.set_page_config(
    page_title="Personal Finance",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Personal Finance")
st.caption("Controle financeiro pessoal – execução local e offline")

# Navegação simples (procedural)
menu = st.sidebar.radio(
    "Navegação",
    ["Dashboard", "Nova Transação", "Histórico"]
)

if menu == "Dashboard":
    render_dashboard()

elif menu == "Nova Transação":
    render_new_transaction()

elif menu == "Histórico":
    render_history()

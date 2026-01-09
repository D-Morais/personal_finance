import streamlit as st
from streamlit_option_menu import option_menu
from ui.dashboard import render_dashboard
from ui.nova_transacao import render_new_transaction
from ui.historico import render_history

st.set_page_config(page_title="Personal Finance", page_icon="💳", layout="wide", initial_sidebar_state="auto")

with st.sidebar:
    pagina = option_menu(
        menu_title="Personal Finance",
        options=["Dashboard", "Nova Transação", "Histórico"],
        icons=["clipboard-data", "plus-lg", "receipt"],
        menu_icon="wallet2",
        default_index=0,
    )

# --- Roteamento ---
if pagina == "Dashboard":
    render_dashboard()

elif pagina == "Nova Transação":
    render_new_transaction()

elif pagina == "Histórico":
    render_history()

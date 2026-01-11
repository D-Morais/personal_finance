import streamlit as st
from repositorio.repositorio_financeiro import adicionar_transacao
from core.classificador import sugestao_categoria


def render_nova_transacao() -> None:

    st.title("➕ Nova Transação")

    if "sugestao" not in st.session_state:
        st.session_state.sugestao = ""

    descricao = st.text_input("Descrição", key="desc")
    # ---- CLASSIFICAÇÃO REAL ----
    if descricao:
        cate, score = sugestao_categoria(descricao)

        if cate:
            st.session_state.sugestao = cate
            st.info(f"💡 Sugestão automática: **{cate}** (score {score})")
        else:
            st.session_state.sugestao = ""
    c1, c2, c3, c4 = st.columns((2, 1, 1, 1))
    cat = c1.text_input("Categoria", value=st.session_state.sugestao)
    valor = c2.number_input("Valor", min_value=0.0)
    tipo = c3.selectbox("Tipo", ["renda", "despesa"])
    data = c4.date_input("Data", format="DD-MM-YYYY")

    if st.button("Salvar"):
        requirementos = [descricao, cat]

        if not all(requirementos):
            st.warning("Necessário preencher todos os campos.")
            return
        adicionar_transacao(descricao, valor, cat, tipo, data)
        st.success("Transação registrada!")
        st.rerun()

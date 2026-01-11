import sqlite3 as sql
from repositorio.script_db import pegar_conexao


def adicionar_transacao(nova_descricao, novo_valor, categoria, transacao, data) -> bool:
    conexao = pegar_conexao()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO transacoes (descricao, valor, categoria, tipo_transacao, data_transacao)
            VALUES (?, ?, ?, ?, ?)
            """, (nova_descricao, novo_valor, categoria, transacao, data)
        )
        conexao.commit()
        return True

    except sql.IntegrityError:
        conexao.rollback()
        return False

    finally:
        conexao.close()


def buscar_todas_transacoes():
    conexao = pegar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM transacoes")

    linhas = cursor.fetchall()
    conexao.close()

    return linhas


def buscar_por_periodo(ano, mes):
    conexao = pegar_conexao()
    cursor = conexao.cursor()
    cursor.execute(
        """
        SELECT * FROM transacoes
        WHERE strftime('%Y', data_transacao) = ?
        AND strftime('%m', data_transacao) = ?
        """, (str(ano), f"{mes:02d}")
    )

    linhas = cursor.fetchall()
    conexao.close()

    return linhas

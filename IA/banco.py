import sqlite3


def conectar_banco():
    return sqlite3.connect("cafe.db")


def criar_tabela():
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS classificacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperatura REAL NOT NULL,
            moagem TEXT NOT NULL,
            torra TEXT NOT NULL,
            qualidade TEXT NOT NULL,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def salvar_classificacao(temperatura, moagem, torra, qualidade):
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO classificacoes
        (temperatura, moagem, torra, qualidade)
        VALUES (?, ?, ?, ?)
    """, (
        temperatura,
        moagem,
        torra,
        qualidade
    ))

    conn.commit()
    conn.close()


def buscar_classificacoes():
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            temperatura,
            moagem,
            torra,
            qualidade,
            data
        FROM classificacoes
        ORDER BY id DESC
    """)

    resultados = cursor.fetchall()

    conn.close()

    return resultados

if __name__ == "__main__":
    criar_tabela()
    print("Banco de dados criado com sucesso!")
import sqlite3
import os


class SenhaModel:

    def __init__(self):
        os.makedirs("database", exist_ok=True)

        self.conexao = sqlite3.connect(
            "database/senhas.db",
            check_same_thread=False
        )

        self.cursor = self.conexao.cursor()

        self.criar_tabelas()


    def criar_tabelas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE,
                senha TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS senhas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER,
                site TEXT,
                email TEXT,
                senha TEXT,
                FOREIGN KEY(usuario_id)
                REFERENCES usuarios(id)
            )
        """)

        self.conexao.commit()


    def cadastrar_usuario(self, usuario, senha):
        try:
            self.cursor.execute(
                "INSERT INTO usuarios(usuario, senha) VALUES (?, ?)",
                (usuario, senha)
            )

            self.conexao.commit()
            return True

        except:
            return False


    def login(self, usuario, senha):
        self.cursor.execute(
            """
            SELECT id
            FROM usuarios
            WHERE usuario = ?
            AND senha = ?
            """,
            (usuario, senha)
        )

        return self.cursor.fetchone()


    def salvar_senha(self, usuario_id, site, email, senha):

        self.cursor.execute(
            """
            INSERT INTO senhas(
                usuario_id,
                site,
                email,
                senha
            )
            VALUES (?, ?, ?, ?)
            """,
            (usuario_id, site, email, senha)
        )

        self.conexao.commit()


    def listar_senhas(self, usuario_id):

        self.cursor.execute(
            """
            SELECT site, email, senha
            FROM senhas
            WHERE usuario_id = ?
            """,
            (usuario_id,)
        )

        return self.cursor.fetchall()
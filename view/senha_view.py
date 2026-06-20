import streamlit as st


class SenhaView:


    def menu(self):

        return st.sidebar.selectbox(
            "Menu",
            [
                "Login",
                "Criar conta"
            ]
        )


    def tela_login(self):

        st.title(" Gerenciador de Senhas")

        usuario = st.text_input("Usuário")
        senha = st.text_input(
            "Senha",
            type="password"
        )

        entrar = st.button("Entrar")

        return usuario, senha, entrar


    def tela_cadastro(self):

        st.title("Criar Conta")

        usuario = st.text_input(
            "Novo usuário"
        )

        senha = st.text_input(
            "Nova senha",
            type="password"
        )

        cadastrar = st.button(
            "Criar conta"
        )

        return usuario, senha, cadastrar


    def tela_cofre(self):

        st.title("Minhas senhas")

        site = st.text_input(
            "Nome do site"
        )

        email = st.text_input(
            "Usuário ou e-mail"
        )

        senha = st.text_input(
            "Senha do site",
            type="password"
        )

        salvar = st.button(
            "Salvar senha"
        )

        return site, email, senha, salvar

import streamlit as st

from controller.senha_controller import SenhaController
from view.senha_view import SenhaView


controller = SenhaController()
view = SenhaView()


# Sessão
if "logado" not in st.session_state:
    st.session_state.logado = False

if "usuario_id" not in st.session_state:
    st.session_state.usuario_id = None


# Usuário deslogado
if not st.session_state.logado:

    opcao = view.menu()


    if opcao == "Login":

        usuario, senha, entrar = view.tela_login()

        if entrar:

            sucesso, usuario_id = controller.entrar(
                usuario,
                senha
            )

            if sucesso:

                st.session_state.logado = True
                st.session_state.usuario_id = usuario_id

                st.success("Login realizado!")
                st.rerun()

            else:
                st.error("Usuário ou senha inválidos")


    else:

        usuario, senha, cadastrar = (
            view.tela_cadastro()
        )


        if cadastrar:

            sucesso, mensagem = (
                controller.criar_conta(
                    usuario,
                    senha
                )
            )

            if sucesso:
                st.success(mensagem)

            else:
                st.error(mensagem)


# Usuário logado
else:

    st.success("Você está logado!")

    site, email, senha, salvar = (
        view.tela_cofre()
    )


    if salvar:

        sucesso = controller.salvar(
            st.session_state.usuario_id,
            site,
            email,
            senha
        )

        if sucesso:
            st.success(
                "Senha salva com sucesso!"
            )

        else:
            st.error(
                "Preencha todos os campos"
            )


    st.subheader("Senhas salvas")

    senhas = controller.buscar_senhas(
        st.session_state.usuario_id
    )


    for site, email, senha in senhas:

        st.write(f" Site: {site}")
        st.write(f" Usuário: {email}")
        st.write(f" Senha: {senha}")
        st.divider()


    if st.button("Sair"):

        st.session_state.logado = False
        st.session_state.usuario_id = None

        st.rerun()

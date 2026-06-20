from model.senha_model import SenhaModel


class SenhaController:

    def __init__(self):
        self.model = SenhaModel()


    def criar_conta(self, usuario, senha):

        if usuario == "" or senha == "":
            return False, "Preencha todos os campos"

        sucesso = self.model.cadastrar_usuario(
            usuario,
            senha
        )

        if sucesso:
            return True, "Conta criada com sucesso"

        return False, "Usuário já existe"


    def entrar(self, usuario, senha):

        dados = self.model.login(
            usuario,
            senha
        )

        if dados:
            return True, dados[0]

        return False, None


    def salvar(self, usuario_id, site, email, senha):

        if not site or not email or not senha:
            return False

        self.model.salvar_senha(
            usuario_id,
            site,
            email,
            senha
        )

        return True


    def buscar_senhas(self, usuario_id):
        return self.model.listar_senhas(usuario_id)
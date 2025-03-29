from ..model.usuario_model import UsuarioModel

def listar_usuarios():
    model = UsuarioModel()
    usuarios = model.get_all_users()
    model.close_connection()
    return usuarios

def cadastrar_usuario(nome, idade, email):
    model = UsuarioModel()
    novo_id = model.insert_user(nome, idade, email)
    model.close_connection()
    return novo_id

def atualizar_usuario(usuario_id, nome, idade, email):
    model = UsuarioModel()
    linhas_afetadas = model.update_user(usuario_id, nome, idade, email)
    model.close_connection()
    return linhas_afetadas

def remover_usuario(usuario_id):
    model = UsuarioModel()
    usuario = model.get_user_by_id(usuario_id)
    model.close_connection()
    return usuario
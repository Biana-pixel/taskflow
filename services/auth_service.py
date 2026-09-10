from werkzeug.security import generate_password_hash, check_password_hash

from models.usuario import criar_usuario, buscar_usuario_por_email


def cadastrar_usuario(nome, email, senha):
    usuario_existente = buscar_usuario_por_email(email)

    if usuario_existente:
        return False, "Este e-mail já está cadastrado."

    senha_hash = generate_password_hash(senha)

    criar_usuario(nome, email, senha_hash)

    return True, "Usuário cadastrado com sucesso."


def autenticar_usuario(email, senha):
    usuario = buscar_usuario_por_email(email)

    if not usuario:
        return None

    senha_valida = check_password_hash(usuario["senha"], senha)

    if not senha_valida:
        return None

    return usuario
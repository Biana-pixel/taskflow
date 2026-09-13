from database.connection import conectar_banco


def criar_usuario(nome, email, senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO usuarios (nome, email, senha)
        VALUES (%s, %s, %s)
        RETURNING id
    """

    cursor.execute(sql, (nome, email, senha))

    usuario_id = cursor.fetchone()[0]

    conexao.commit()

    cursor.close()
    conexao.close()

    return usuario_id


def buscar_usuario_por_email(email):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql = """
        SELECT id, nome, email, senha
        FROM usuarios
        WHERE email = %s
    """

    cursor.execute(sql, (email,))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if resultado:
        return {
            "id": resultado[0],
            "nome": resultado[1],
            "email": resultado[2],
            "senha": resultado[3]
        }

    return None
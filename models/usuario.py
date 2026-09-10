from database.connection import conectar_banco
from psycopg2.extras import RealDictCursor


def criar_usuario(nome, email, senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO usuarios (nome, email, senha)
        VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (nome, email, senha))

    conexao.commit()

    cursor.close()
    conexao.close()


def buscar_usuario_por_email(email):
    conexao = conectar_banco()
    cursor = conexao.cursor(cursor_factory=RealDictCursor)

    sql = """
        SELECT id, nome, email, senha
        FROM usuarios
        WHERE email = %s
    """

    cursor.execute(sql, (email,))

    usuario = cursor.fetchone()

    cursor.close()
    conexao.close()

    return usuario
from database.connection import conectar_banco


def criar_tarefa(titulo, descricao, prioridade, status, prazo, usuario_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO tarefas (
            titulo,
            descricao,
            prioridade,
            status,
            prazo,
            usuario_id
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(
        sql,
        (
            titulo,
            descricao,
            prioridade,
            status,
            prazo,
            usuario_id
        )
    )

    conexao.commit()

    cursor.close()
    conexao.close()


def listar_tarefas(usuario_id):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM tarefas
        WHERE usuario_id = %s
        ORDER BY id DESC
    """, (usuario_id,))

    tarefas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return tarefas


def buscar_tarefa(id, usuario_id):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM tarefas
        WHERE id = %s
        AND usuario_id = %s
    """, (id, usuario_id))

    tarefa = cursor.fetchone()

    cursor.close()
    conexao.close()

    return tarefa


def atualizar_tarefa(
    id,
    titulo,
    descricao,
    prioridade,
    status,
    prazo,
    usuario_id
):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE tarefas
        SET
            titulo = %s,
            descricao = %s,
            prioridade = %s,
            status = %s,
            prazo = %s
        WHERE id = %s
        AND usuario_id = %s
    """, (
        titulo,
        descricao,
        prioridade,
        status,
        prazo,
        id,
        usuario_id
    ))

    conexao.commit()

    cursor.close()
    conexao.close()


def excluir_tarefa(id, usuario_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM tarefas
        WHERE id = %s
        AND usuario_id = %s
    """, (id, usuario_id))

    conexao.commit()

    cursor.close()
    conexao.close()
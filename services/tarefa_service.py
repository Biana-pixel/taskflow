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
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT *
        FROM tarefas
        WHERE usuario_id = %s
        ORDER BY id DESC
    """, (usuario_id,))

    resultados = cursor.fetchall()

    tarefas = []

    for resultado in resultados:
        tarefa = {
            "id": resultado[0],
            "titulo": resultado[1],
            "descricao": resultado[2],
            "prioridade": resultado[3],
            "status": resultado[4],
            "prazo": resultado[5],
            "usuario_id": resultado[6]
        }
        tarefas.append(tarefa)

    cursor.close()
    conexao.close()

    return tarefas


def buscar_tarefa(id, usuario_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT *
        FROM tarefas
        WHERE id = %s
        AND usuario_id = %s
    """, (id, usuario_id))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if resultado:
        return {
            "id": resultado[0],
            "titulo": resultado[1],
            "descricao": resultado[2],
            "prioridade": resultado[3],
            "status": resultado[4],
            "prazo": resultado[5],
            "usuario_id": resultado[6]
        }

    return None


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
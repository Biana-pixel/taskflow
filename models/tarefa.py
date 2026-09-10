class Tarefa:

    def __init__(
        self,
        id=None,
        titulo=None,
        descricao=None,
        prioridade="media",
        status="pendente",
        prazo=None,
        usuario_id=None
    ):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = status
        self.prazo = prazo
        self.usuario_id = usuario_id
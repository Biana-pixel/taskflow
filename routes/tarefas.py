from flask import Blueprint, request, redirect, url_for, render_template, session
from services.tarefa_service import (
    criar_tarefa,
    listar_tarefas,
    buscar_tarefa,
    atualizar_tarefa,
    excluir_tarefa
)


tarefas = Blueprint("tarefas", __name__)


@tarefas.route("/tarefas")
def listar():

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    lista_tarefas = listar_tarefas(session["usuario_id"])

    return render_template(
        "tarefas.html",
        tarefas=lista_tarefas
    )


@tarefas.route("/tarefas/criar", methods=["POST"])
def criar():

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    titulo = request.form.get("titulo")
    descricao = request.form.get("descricao")
    prioridade = request.form.get("prioridade")
    status = request.form.get("status")
    prazo = request.form.get("prazo")

    if not prioridade:
        prioridade = "media"

    if not status:
        status = "pendente"

    criar_tarefa(
        titulo,
        descricao,
        prioridade,
        status,
        prazo,
        session["usuario_id"]
    )

    return redirect(url_for("tarefas.listar"))


@tarefas.route("/tarefas/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    tarefa = buscar_tarefa(id, session["usuario_id"])

    if not tarefa:
        return redirect(url_for("tarefas.listar"))

    if request.method == "POST":

        titulo = request.form.get("titulo")
        descricao = request.form.get("descricao")
        prioridade = request.form.get("prioridade")
        status = request.form.get("status")
        prazo = request.form.get("prazo")

        atualizar_tarefa(
            id,
            titulo,
            descricao,
            prioridade,
            status,
            prazo,
            session["usuario_id"]
        )

        return redirect(url_for("tarefas.listar"))

    return render_template(
        "editar_tarefa.html",
        tarefa=tarefa
    )


@tarefas.route("/tarefas/excluir/<int:id>", methods=["POST"])
def excluir(id):

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    excluir_tarefa(
        id,
        session["usuario_id"]
    )

    return redirect(url_for("tarefas.listar"))
from flask import Blueprint, render_template, request, redirect, url_for, session

from services.auth_service import cadastrar_usuario, autenticar_usuario


auth = Blueprint("auth", __name__)


@auth.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    mensagem = None

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")

        if not nome or not email or not senha:
            mensagem = "Preencha todos os campos."
            return render_template("cadastro.html", mensagem=mensagem)

        sucesso, mensagem = cadastrar_usuario(nome, email, senha)

        if sucesso:
            return redirect(url_for("auth.login"))

    return render_template("cadastro.html", mensagem=mensagem)


@auth.route("/login", methods=["GET", "POST"])
def login():
    mensagem = None

    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        usuario = autenticar_usuario(email, senha)

        if usuario:
            session["usuario_id"] = usuario["id"]
            session["usuario_nome"] = usuario["nome"]

            return redirect(url_for("dashboard.index"))

        mensagem = "E-mail ou senha inválidos."

    return render_template("login.html", mensagem=mensagem)


@auth.route("/logout")
def logout():
    session.clear()

    return redirect(url_for("auth.login"))
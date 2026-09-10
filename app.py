from flask import Flask, render_template

from config import Config
from database.connection import conectar_banco

from routes.auth import auth
from routes.dashboard import dashboard
from routes.tarefas import tarefas


app = Flask(__name__)
app.config.from_object(Config)


# Registra as rotas
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(tarefas)


@app.route("/")
def inicio():
    return render_template("inicio.html")


@app.route("/teste-banco")
def teste_banco():

    conexao = None

    try:
        conexao = conectar_banco()

        if conexao.is_connected():
            return render_template(
                "teste_banco.html",
                sucesso=True
            )

        return render_template(
            "teste_banco.html",
            sucesso=False
        )

    except Exception as erro:
        return render_template(
            "teste_banco.html",
            sucesso=False,
            erro=erro
        )

    finally:

        if conexao is not None and conexao.is_connected():
            conexao.close()


if __name__ == "__main__":
    app.run(debug=True)
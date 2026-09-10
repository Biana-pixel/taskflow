from flask import Flask, render_template

from config import Config
from database.connection import conectar_banco, criar_tabelas

from routes.auth import auth
from routes.dashboard import dashboard
from routes.tarefas import tarefas


app = Flask(__name__)
app.config.from_object(Config)


# Cria as tabelas do TaskFlow no banco
try:
    criar_tabelas()
except Exception as erro:
    print(f"Erro ao criar tabelas: {erro}")


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

        return render_template(
            "teste_banco.html",
            sucesso=True
        )

    except Exception as erro:
        return render_template(
            "teste_banco.html",
            sucesso=False,
            erro=erro
        )

    finally:

        if conexao is not None:
            conexao.close()


if __name__ == "__main__":
    app.run(debug=True)
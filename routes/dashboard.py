from flask import Blueprint, render_template, session, redirect, url_for


dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/dashboard")
def index():

    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template(
        "dashboard.html",
        nome=session.get("usuario_nome")
    )
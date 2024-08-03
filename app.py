from flask import Flask, render_template, redirect, request, url_for

from forms import WydatekForm
from models import Wydatki

app = Flask(__name__)


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "blablabla"
    wydatki = Wydatki()
    error = ""

    @app.route("/", methods=["GET", "POST"])
    def index():
        form = WydatekForm()
        if request.method == "POST":
            if form.validate_on_submit():
                wydatki.create(form.data)
                wydatki.save_all()
            return redirect(url_for("index"))

        return render_template("index.html", form=form, lista_wydatkow=wydatki.get_all(), error=error)

    @app.route("/delete", methods=["POST"])
    def delete():
        if request.method == "POST":
            wydatek_id = int(request.form.get('index')) - 1
            wydatki.remove(wydatek_id)
            wydatki.save_all()
            return redirect(url_for("index"))

    @app.route("/edit", methods=["POST"])
    def edit():
        if request.method == "POST":
            wydatek_id = int(request.form.get('index')) - 1
            form = WydatekForm(data=request.form)

            if form.validate_on_submit():
                wydatki.update(wydatek_id, form.data)
                return redirect(url_for("index"))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

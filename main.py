from flask import Flask, render_template, redirect, request, url_for

from forms import WydatekForm
from models import Wydatki


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "blablabla"
    wydatki = Wydatki()
    error = ""

    @app.route("/", methods=["GET", "POST"])
    def index():
        form = WydatekForm()
        error = ""

        if request.method == "POST":
            if form.validate_on_submit():
                wydatki.create(form.data)
                wydatki.save_all()
            return redirect(url_for("index"))

        return render_template("index.html", form=form, lista_wydatkow=wydatki.get_all(), error=error)


    return app



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

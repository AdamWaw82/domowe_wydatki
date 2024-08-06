import json

from flask import Flask, render_template, redirect, request, url_for, jsonify, abort

from forms import WydatekForm
from models import Wydatki

app = Flask(__name__)


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "blablabla"

    wydatki = Wydatki()
    error = ""

    @app.route("/api/v1/wydatki/", methods=["GET"])
    def list_api_v1():
        response = json.dumps(wydatki.get_all(), default=str)
        return jsonify(response)

    @app.route("/api/v1/wydatki/<int:id>", methods=["GET"])
    def get_wydatki(id):
        wydatek = wydatki.get(id)
        if not wydatek:
            abort(404)
        response = json.dumps(wydatek, default=str)
        return jsonify(response)

    @app.route("/api/v1/wydatki/", methods=["POST"])
    def create_wydatek():
        form = WydatekForm()
        if form.validate_on_submit():
            wydatki.create(form.data)
            wydatki.save_all()
        return redirect(url_for("index"))

    @app.route("/api/v1/wydatki/<int:id>", methods=['DELETE'])
    def delete_wydatek(id):
        result = wydatki.remove(id)
        if not result:
            abort(404)
        return jsonify({'result': result})

    @app.route("/api/v1/wydatki/<int:id>", methods=["PUT"])
    def update_wydatek(id):
        if not request.json:
            abort(400)

        data = request.json
        form = WydatekForm(data=data)

        if form.validate():
            result = wydatki.modify(index=id, data=form.data)
            return jsonify({'result': result})
        else:
            abort(500)

    @app.route("/", methods=["GET"])
    def index():
        form = WydatekForm()
        return render_template("index.html", form=form, error=error)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

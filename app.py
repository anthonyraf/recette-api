from flask import Flask
from flask import jsonify, Response
from recette import Recette, ListeRecettes

app: Flask = Flask(__name__)


@app.route("/")
def index() -> str:
    return '<h1>Hello World!</h1>'


@app.route("/api/recette/<nom_recette>", methods=["GET"])
def recette(nom_recette: str) -> Response:
    liste_recettes = ListeRecettes()

    liste_recettes.add(
        Recette("Pizza", "une pizza", ["farine", "fromage", "..."]),
        Recette("Tarte aux pommes", "une tarte avec des pommes", ["farine", "pommes", "..."])
    )
    recette = liste_recettes.get(nom_recette)

    if not recette:
        app.aborter(404)

    return jsonify(recette)
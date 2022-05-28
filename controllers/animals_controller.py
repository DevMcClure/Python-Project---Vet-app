from flask import Flask, render_template
from repositories import animal_repository
from repositories import vet_repository
from models.animal import Animal
from models.vet import Vet
from flask import Blueprint

animals_blueprint = Blueprint("animals", __name__)


@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all()
    return render_template("animals/index.html", animals = animals)



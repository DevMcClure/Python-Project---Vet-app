from atexit import register
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import animal_repository
from repositories import vet_repository
from models.animal import Animal
from models.vet import Vet


animals_blueprint = Blueprint("animals", __name__)


@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all()
    return render_template("animals/index.html", all_animals = animals)


@animals_blueprint.route("/register/animal") 
def register_animals():
    register_animal = animal_repository.select_all()
    return render_template("animals/register_animal.html", all_register_animals = register_animal )




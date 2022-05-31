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


@animals_blueprint.route("/register/animal", methods= ['Get'])
def register_animals():
    register_animal = animal_repository.select_all()
    return render_template("animals/register_animal.html", all_register_animals = register_animal)


@animals_blueprint.route("/animal/info/<id>", methods=['GET'])
def animal_info(id):
    animal= animal_repository.select(id)
    return render_template("animals/animal_info.html", animal = animal)



@animals_blueprint.route("/animal/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect('/animals')


@animals_blueprint.route("/animal/<id>/edit", methods=['GET'])
def edit_animal(id):
    animal = animal_repository.select(id)
    vets = vet_repository.select_all()
    return render_template("animals/edit.html", animal = animal, all_vets= vets)   
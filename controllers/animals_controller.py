from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import animal_repository
from repositories import vet_repository
from models.animal import Animal


animals_blueprint = Blueprint("animals", __name__)


@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all()
    return render_template("animals/index.html", all_animals = animals)


@animals_blueprint.route("/register/animal", methods= ['Get'])
def register_animals():
    vets = vet_repository.select_all()
    return render_template("animals/register_animal.html", all_vets = vets)

# CREATE
# POST '/animals'

@animals_blueprint.route("/animals",  methods=['POST'])
def create_pet():
    animal_name = request.form['animal_name']
    vet_id     = request.form['vet_id']
    date_of_birth = request.form['date_of_birth']
    animal_type   = request.form['animal_type']
    owner_contact = request.form['owner_contact']
    treatment_notes = request.form['treatment_notes']

    vet        = vet_repository.select(vet_id)
    animal        = Animal(animal_name, vet,date_of_birth, animal_type, owner_contact, treatment_notes)

    animal_repository.save(animal)
    return redirect('/animals')


@animals_blueprint.route("/animal/<id>/info", methods=['GET'])
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
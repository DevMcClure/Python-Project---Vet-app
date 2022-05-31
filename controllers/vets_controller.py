from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import animal_repository
from repositories import vet_repository
from models.animal import Animal
from models.vet import Vet


vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/vet_info.html", all_vets = vets)



@vets_blueprint.route("/vet/<id>/delete", methods=['POST'])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect('/vets')



@vets_blueprint.route("/new/vet", methods= ['GET'])
def new_vet():
    vets = vet_repository.select_all()
    return render_template("vets/new_vet.html", all_vets = vets)



@vets_blueprint.route("/vets",  methods=['POST'])
def create_vet():
    first_name = request.form['first_name']
    second_name = request.form['second_name']
   
    vet = Vet(first_name, second_name)
   
    vet_repository.save(vet)
    return redirect('/vets')    

from flask import FLASK, render_template
from repositories import animal_repository
from repositories import vet_repository
from models.animal import Animal
from flask import Blueprint

animals_blueprint = Blueprint("animals", __name__)
from flask import FLASK, render_template
from repositories import animal_repository
from repositories import vet_repository
from models.vet import Vet
from flask import Blueprint 

vets_blueprint = Blueprint("animals", __name__)



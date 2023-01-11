from flask import (Blueprint, render_template)
import json, pprint

bp = Blueprint('pet', __name__, url_prefix="/pets")

pets = json.load(open('pets.json'))
pprint.pprint(pets)

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)


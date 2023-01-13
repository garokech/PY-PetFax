from flask import ( Blueprint, render_template ) 

bp = Blueprint('facet', __name__, url_prefix="/facts")

@bp.route('/new')
def new(): 
    return render_template('facts/new.html')

@bp.route('/', methods=['POST'])
def index():
    print(request.form)
    return 'Thanks for submitting that fact!'
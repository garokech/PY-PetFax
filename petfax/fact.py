from flask import ( Blueprint, render_template, redirect ) 

bp = Blueprint('facet', __name__, url_prefix="/facts")

@bp.route('/new')
def new(): 
    return render_template('facts/new.html')

@bp.route('/', methods=['GET','POST'])
def index(): 
    if request.method == 'POST':
       print(request.form)
       return redirect('/facts')
    
    return 'This is the facts index'


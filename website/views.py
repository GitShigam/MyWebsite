from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')           
def home():                 
     
    return render_template("home.html")

@views.route('/CV')
def cv():

    return render_template("cv.html")

@views.route('/projects')
def projects():

    return render_template("projects.html")
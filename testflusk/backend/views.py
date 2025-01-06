from flask import Blueprint, render_template

# Create a Blueprint object
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')
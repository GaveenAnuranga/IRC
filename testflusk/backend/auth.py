from flask import Blueprint, render_template, request, flash
import mysql.connector

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        lemail = request.form.get('email')
        lpassword = request.form.get('pw')
    return render_template('login.html')

@auth.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@auth.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':
        cemail = request.form.get('email')
        name = request.form.get('name')
        massage = request.form.get('massage')
    return render_template('contact.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('fname')
        lastName = request.form.get('lname')
        password1 = request.form.get('pw1')
        password2 = request.form.get('pw2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            flash('Account created', category='success')

       

        

    return render_template('signup.html')
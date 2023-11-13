from flask import Blueprint, render_template, request, flash,redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .dbmodels import User
from . import views

auth = Blueprint('auth',__name__)

@auth.route('/login', methods = ['GET','POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email = email).first()
    if user:
      if check_password_hash(user.password, password):
        flash('You have successfully logged in', category ='success')
        return redirect(url_for('views.home'))
      else:
        flash('Incorrect password', category = 'error')
    else:
      flash('Incorrect email', category = 'error')
  return render_template("login.html")

@auth.route('/logout')
def logout():
  return redirect(url_for('auth.login'))
  

@auth.route('/sign-up', methods = ['GET','POST'])
def sign_up():
  if request.method == 'POST':
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    user = User.query.filter_by(email = email).first()
    if user:
      flash('Account already exists', category = 'error')  
    elif len(email)<4:
      flash('Email must be greater than 3 characters.', category = 'error') #category assignment used to pass into html
    elif len(first_name)<2:
      flash('First name must be greater than 1 character.', category = 'error')
    elif len(password)<7:
      flash('Password must be greater than 6 characters.', category = 'error')
    elif password != password2:
      flash('Passwords dont match', category = 'error')
    else:
      new_user = User(email = email, first_name = first_name, password = generate_password_hash(password,method='scrypt', salt_length=16))
      db.session.add(new_user)
      db.session.commit()
      flash('Account created' , category = 'success')

      return redirect(url_for('auth.login'))
      
      
  
  return render_template("sign-up.html")


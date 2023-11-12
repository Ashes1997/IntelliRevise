from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods = ['GET','POST'])
def login():
  return render_template("login.html")

@auth.route('/logout')
def logout():
  return render_template("logout.html") #going to change, need to redirect
  

@auth.route('/sign-up', methods = ['GET','POST'])
def sign_up():
  if request.method == 'POST':
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if len(email)<4:
      flash('Email must be greater than 3 characters.', category = 'error') #category assignment used to pass into html
    elif len(first_name)<2:
      flash('First name must be greater than 1 character.', category = 'error')
    elif len(password)<7:
      flash('Password must be greater than 6 characters.', category = 'error')
    elif password != password2:
      flash('Passwords dont match', category = 'error')
    else:
      flash('Account created' , category = 'success')
      
  
  return render_template("sign-up.html")


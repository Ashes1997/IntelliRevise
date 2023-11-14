from flask import Blueprint, render_template
import flask_login
from flask_login import current_user

views = Blueprint('views',__name__)

@views.route('/')
@flask_login.login_required
def home():
  return render_template("home.html", user=current_user)

@views.route('/try-it-out')
def try_it_out():
  return render_template("try_it_out.html")

  




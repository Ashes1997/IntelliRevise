from flask import Blueprint, render_template, request, flash,redirect, url_for
import flask_login
from flask_login import current_user
from chatGPT import flash_create
import random


views = Blueprint('views',__name__)

@views.route('/')
@flask_login.login_required
def home():
  return render_template("home.html", user=current_user)

@views.route('/try-it-out', methods = ['GET','POST'])
def try_it_out():
  if request.method == 'POST':
    prompt = request.form.get('note')
    if len(prompt) >= 300:
      flash('Note must be less than 300 characters', category = "error")
    else: 
      flashcard = flash_create(prompt)
      
        #index 0 is question
        #index 1 is correct answer
        #index 2 is incorrect answer 1
        #index 3 is incorrect answer 2
        #index 4 is incorrect answer 3
      question = flashcard[0]
      answers = [(flashcard[1],True), (flashcard[2], False), (flashcard[3], False), (flashcard[4], False)]
      shuffled_answers = random.shuffle(answers)
      return render_template("try_it_out.html", user=current_user, question=question, answers=shuffled_answers)
    
  
  
  
  
  return render_template("try_it_out.html", user=current_user)


  




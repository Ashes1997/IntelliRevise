from flask import Blueprint, render_template, request, flash,redirect, url_for
import flask_login
from flask_login import current_user
from chatGPT import flash_create
import random


views = Blueprint('views',__name__)

@views.route('/')
def home():
  return render_template("home.html", user=current_user)

@views.route('/try-it-out', methods = ['GET','POST'])
def try_it_out(): 
  if request.method == 'POST':
    if request.form.get('submit_button') == 'create_flashcard': 
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
        correct_answer = flashcard[1]
        answers = [flashcard[1], flashcard[2], flashcard[3], flashcard[4]]
        random.shuffle(answers)
        return render_template("try_it_out.html", user=current_user, question=question, answers=answers, correct_answer=correct_answer)
    elif request.form.get('submit_button') == 'submit_answer':
      print(request.form)
      answer = request.form.get('answer')
      correct_answer = request.form.get('correct_answer')
      if answer == correct_answer:
        return redirect(url_for('views.try_it_out_success'))
      else :
        flash('Incorrect answer, try again!', category = "error")
    
  
  
  
  
  return render_template("try_it_out.html", user=current_user)



@views.route('/try-it-out/success', methods = ['GET','POST'])
def try_it_out_success():
  return render_template("try_it_out_success.html", user=current_user)



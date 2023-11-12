import openai
import os
from openai import OpenAI


client = OpenAI()
def flash_create(prompt: str):

  
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a tutor that creates flashcards for your students in the following format. Question:..\nCorrect Answer:..\nIncorrect Answer 1:..\nIncorrect Answer 2:..\nIncorrect Answer 3:..\n. Do not deviate from this format. The questions and answers are based off the submitted text and should be no longer than 50 words each. You rely heavily on the given text and rely little on external information."},
      {"role": "user", "content": prompt}
    ]
  )
  #index 0 is question
  #index 1 is correct answer
  #index 2 is incorrect answer 1
  #index 3 is incorrect answer 2
  #index 4 is incorrect answer 3
  prompt_return = completion.choices[0].message.content
  flashcard = prompt_return.split("\n") #splits prompt into array
  
  # untrimmed_q= flashcard[0] #code for trimming q
  # trimmed_q = untrimmed_q.replace("Question: ","")
  # flashcard[0]=trimmed_q
  
  # untrimmed_a=flashcard[1]
  #for loops in java > for loops in python
  for index, value in enumerate(flashcard):
    trimmed = value.replace("Question: ","").replace("Correct Answer: ","").replace("Incorrect Answer 1: ","").replace("Incorrect Answer 2: ","").replace("Incorrect Answer 3: ","")
    flashcard[index]=trimmed
  
  return flashcard


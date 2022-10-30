
from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank =[Question(x['text'],x['answer'])for x in question_data]
print(question_bank)






quiz = Quiz(question_bank)
#quiz.nextquestion()
while quiz.still_has_question():
    quiz.nextquestion()
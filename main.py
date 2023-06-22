from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

#create question bank and initialize
question_bank=[]
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]['text'], question_data[i]['answer']))

random.shuffle(question_bank)
quiz=QuizBrain(question_bank)
#quiz.next_question()
#quiz.next_question()
#quiz.next_question()
#quiz.next_question()
#quiz.next_question()
#quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()
quiz.final_score()

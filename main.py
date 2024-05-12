from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for que in question_data:
    question = que['question']
    correct_answer = que['correct_answer']
    new_q = Questions(question, correct_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

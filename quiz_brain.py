import html
class QuizBrain:
    def __init__(self, qlist):
        self.user_answer = None
        self.score = 0
        self.question_number = 0
        self.question_list = qlist

    def still_has_question(self):
        q_length = len(self.question_list)
        return self.question_number < q_length

    def next_question(self, ):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_question(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

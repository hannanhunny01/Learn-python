class Quiz:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list= question_list
        self.correct=0

    def nextquestion(self):
        currentquestion = self.question_list[self.question_number]
        self.question_number+=1
        user_answer = input(f'Question No.{self.question_number}:{currentquestion.text}(True/False):')
        self.check_answer(user_answer,currentquestion.answer)
    def still_has_question(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            return False
    def check_answer(self,user_answer,currentanswer):
        if user_answer.lower() == currentanswer.lower():
            self.correct+=1
            print("you got it Right")
        else:
            print('you got it wrong')

        print(f'you score is {self.correct}/{self.question_number}')
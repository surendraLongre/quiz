class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0

    def next_question(self):
        self.question_number+=1
        user_input=input(f"Q.{self.question_number} {self.question_list[self.question_number-1].text}(True/False): ").lower()
        correct_answer=self.question_list[self.question_number-1].answer.lower()
        self.check_answer(user_input, correct_answer)
        

    def still_has_question(self):
        return self.question_number!=len(self.question_list)
    

    def check_answer(self, user_input, correct_answer):
        if user_input==correct_answer:
            self.score+=1
            print("you got it right!")
            print(f"Your current score is: {self.score}")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")

    def final_score(self):
        print(f"The quiz has finished.")
        print(f"Your final score is {self.score}/{self.question_number}.\n")


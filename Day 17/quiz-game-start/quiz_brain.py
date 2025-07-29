class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions = q_list
        self.current_question = self.questions[self.question_number]
        self.questions_answered = []
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions)
    
    def next_question(self):
        self.question_number += 1
        if self.question_number < len(self.questions):
            self.current_question = self.questions[self.question_number]
    
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer.lower()
        self.next_question()
        if user_answer == correct_answer:
            self.score += 1
            print(f"You got it right!\nThe correct answer was: {correct_answer.capitalize()}")
            return True
        else:
            print(f"That's wrong.\nThe correct answer was: {correct_answer.capitalize()}.")
            return False

    def ask_question(self):
        self.user_answer = input(f"Q.{self.question_number + 1}: {self.current_question.text} (True/False): ").lower()
        self.questions_answered.append(self.current_question.text)
        self.check_answer(self.user_answer)
        print(f"Your current score is: {self.score}/{len(self.questions_answered)}")
from subjects.models import Subjects, SubTopic , Question

class Validation:
    def __init__(self):
        self.array = []
        self.number_of_question = 0
        self.number_of_correct_answer = 0
        self.number_of_wrong_answer = 0

    def checkAnswer(self, question, provide_answer):
        temp = {}
        self.number_of_question += 1
        temp["question"] = question.question
        temp["correct_answer"] = question.correct_answer
        temp["provide_answer"] = provide_answer

        if question.correct_answer == provide_answer:
            self.number_of_correct_answer += 1
            temp["status"] = "correct"
        else:
            self.number_of_wrong_answer += 1
            temp["status"] = "wrong"
        self.array.append(temp)

    def getResult(self):
        return self.array

    def Percentage_of_success(self):
        return (self.number_of_correct_answer / self.number_of_question) * 100

    def Percentage_of_failier(self):
        return (self.number_of_wrong_answer / self.number_of_question) * 100







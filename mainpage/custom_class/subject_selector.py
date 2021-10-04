from subjects.models import Subjects, SubTopic , Question
import random


class SubjectSelection:
    i = 0  # static variables

    def __init__(self):
        self.info = None
        # self.list_of_question = None
        self.final = []

    def __getAllQuestion(self):
        return set(self.info.question_set.all())

    def __typeConterter(self, parameter):
        return set(parameter)

    def __shuffler(self,array):  # reference type
        random.shuffle(array)

    def getQuesion(self,id):
        subject = Question.objects.filter(id=id).first()
        return subject


    def __gradQuestionInfomation(self, question):
        dictionary = {}
        ss = []  # create simple

        dictionary["id"] = question.id
        dictionary["question"] = question.question
        dictionary["answer"] = question.correct_answer
        ss = [x.other_ansewr for x in question.otheranswer_set.all()]
        ss.append(question.correct_answer)

        self.__shuffler(ss)

        dictionary["other_answer"] = ss
        return dictionary

    def __readOtheranswer(self, list):
        for quesiton in list:
            self.final.append(self.__gradQuestionInfomation(quesiton))

    def getSample(self, id, sample_size):
        self.info = SubTopic.objects.filter(id=id).first()
        if not self.__validation(self.info):
            return False
        all_quesiton = self.__typeConterter(self.__getAllQuestion())
        random_selection = self.__selecte_random(all_quesiton, sample_size)
        self.__readOtheranswer(random_selection)
        return self.final

    def __selecte_random(self, population, sample):
        if sample > len(population) or sample < 0:
            return random.sample(population, len(population))
        return random.sample(population, sample)

    def __validation(self, parameter):
        if parameter is None:
            return False
        return True

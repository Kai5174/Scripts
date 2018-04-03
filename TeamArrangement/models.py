class Person:
    def __init__(self, name):
        self.__name = name
        self.__duty = []    # list contains Question object
        self.__query = []   # list contains Question object

    def add_duty(self, duty):
        duty.add_dutier(self)
        if duty in self.__duty:
            pass
        else:
            self.__duty.append(duty)

    def del_duty(self, duty):
        duty.del_dutier(self)
        if duty in self.__duty:
            self.__duty.remove(duty)
        else:
            pass

    def add_query(self, query):
        query.add_querier(self)
        if query in self.__query:
            pass
        else:
            self.__query.append(query)

    def del_query(self, query):
        query.del_querier(self)
        if query in self.__query:
            self.__query.remove(query)
        else:
            pass

    def get_duty(self):
        return self.__duty

    def get_query(self):
        return self.__query

    def get_name(self):
        return self.__name

    def num_duty(self):
        return len(self.__duty)

    def num_query(self):
        return len(self.__query)

    def __str__(self):
        return self.get_name()

    def __repr__(self):
        return self.get_name()


class Question:
    def __init__(self, ques):
        self.__question = ques      # str
        self.__dutier = []          # list contains Person object
        self.__querier = []         # list contains Person object

    def add_dutier(self, dutier):
        if dutier in self.__dutier:
            print("due dutier {}".format(dutier))
            pass
        else:
            self.__dutier.append(dutier)

    def del_dutier(self, dutier):
        if dutier in self.__dutier:
            self.__dutier.remove(dutier)
        else:
            pass

    def add_querier(self, querier):
        if querier in self.__querier:
            print("due querier {}".format(querier))
            pass
        else:
            self.__querier.append(querier)

    def del_querier(self, querier):
        if querier in self.__querier:
            self.__querier.remove(querier)
        else:
            pass

    def num_dutier(self):
        return len(self.__dutier)

    def num_querier(self):
        return len(self.__querier)

    def get_question(self):
        return self.__question

    def get_querier(self):
        return self.__querier

    def get_dutier(self):
        return self.__dutier

    def __str__(self):
        return self.get_question()

    def __repr__(self):
        return self.get_question()


class Strategy:
    def __init__(self, persons, questions):
        self.persons_bak = persons.copy()        # List Person()
        self.questions_bak = questions.copy()    # List Question()
        self.persons_seg = persons.copy()
        self.questions_seg = questions.copy()

    def __segmentation_restore(self):
        self.persons_seg = self.persons_bak.copy()        # List Person()
        self.questions_seg = self.questions_bak.copy()      # List Question()

    def find_the_most_popular_question(self):
        best_que = self.questions_seg[0]
        for que in self.questions_seg:
            if best_que.num_querier() < que.num_querier():
                best_que = que
        return best_que

    def segmentation_update(self, del_ppl_list):
        for que in self.questions_seg:
            for ppl in del_ppl_list:
                que.del_querier(ppl)

    def round_update(self, del_que_list):
        for ppl in self.persons_bak:
            for que in del_que_list:
                ppl.del_query(que)
        self.__segmentation_restore()

    def maximized_strategy(self):
        strategy = {}       # I would like to store the strategy in {round: group} dictionary
        iround = 0
        while self.find_the_most_popular_question().num_querier() > 0:
            iround += 1
            tmp_solved_question_list = []
            while self.find_the_most_popular_question().num_querier() > 0:
                most_popular_question = self.find_the_most_popular_question()
                tmp_solved_question_list.append(most_popular_question)
                dutiers = most_popular_question.get_dutier()
                queriers = most_popular_question.get_querier()
                self.segmentation_update(dutiers + queriers)
            strategy[iround] = tmp_solved_question_list
            self.round_update(strategy[iround])
            print(self.find_the_most_popular_question().num_querier())
        return strategy


if __name__ == "__main__":
    ROLES_LIST = ['Kai', 'Jacky', 'Yikai', 'Guangchen', 'Xueyuan', 'Sophie']
    QUESTIONS_LIST = ['2.44', '2.45', '2.49', '2.51', '2.54', '2.56']
    person = {name: Person(name=name) for name in ROLES_LIST}
    question = {que: Question(ques=que) for que in QUESTIONS_LIST}

    print("Testing add_duty in Persion...You should see all question has dutier correspondently")
    for ii in range(len(ROLES_LIST)):
        person[ROLES_LIST[ii]].add_duty(question[QUESTIONS_LIST[ii]])
        print("Question {} has dutier: {}".format(QUESTIONS_LIST[ii], question[QUESTIONS_LIST[ii]].get_dutier()))

    print("Testing del_duty in Person...You should see all question does not have dutier")
    for ii in range(len(ROLES_LIST)):
        person[ROLES_LIST[ii]].del_duty(question[QUESTIONS_LIST[ii]])
        print("Question {} has dutier: {}".format(QUESTIONS_LIST[ii], question[QUESTIONS_LIST[ii]].get_dutier()))

    print("Testing add_query in Persion...You should see all question has querier correspondently")
    for ii in range(len(ROLES_LIST)):
        person[ROLES_LIST[ii]].add_query(question[QUESTIONS_LIST[ii]])
        print("Question {} has query: {}".format(QUESTIONS_LIST[ii], question[QUESTIONS_LIST[ii]].get_querier()))

    print("Testing del_duty in Person...You should see all question does not have querier")
    for ii in range(len(ROLES_LIST)):
        person[ROLES_LIST[ii]].del_query(question[QUESTIONS_LIST[ii]])
        print("Question {} has query: {}".format(QUESTIONS_LIST[ii], question[QUESTIONS_LIST[ii]].get_querier()))

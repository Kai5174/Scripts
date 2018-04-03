from models import Question, Person, Strategy

ROLES_LIST = ['Kai', 'Jacky', 'Yikai', 'Guangchen', 'Xueyuan', 'Sophie']
QUESTIONS_LIST = ['2.44', '2.45', '2.49', '2.51', '2.54', '2.55', '2.56', '2.63', '2.65', '2.67']
DUTY = {
    'Kai': ['2.44'],
    'Guangchen': ['2.67'],
    'Yikai': ['2.45', '2.65'],
    'Xueyuan': ['2.49', '2.63'],
    'Sophie': ['2.51', '2.56'],
    'Jacky': ['2.54', '2.55'],
}

QUERY = {
    'Kai': ['2.45', '2.54', '2.55'],
    'Guangchen': ['2.56', '2.63', '2.65', '2.67'],
    'Yikai': ['2.49', '2.51', '2.55'],
    'Xueyuan': ['2.44', '2.54', '2.63'],
    'Sophie': ['2.67', '2.65', '2.55', '2.51'],
    'Jacky': ['2.49', '2.45', '2.65', '2.56'],
}

print("Initializing Person() and Question() ...")

person = {name: Person(name=name) for name in ROLES_LIST}
question = {que: Question(ques=que) for que in QUESTIONS_LIST}

person_list = []
question_list = []

for value in person:
    person_list.append(person[value])

for value in question:
    question_list.append(question[value])

for __ppl in ROLES_LIST:
    for __duty in DUTY[__ppl]:
        person[__ppl].add_duty(question[__duty])

# Manually input at each running,
# print("Input duties of each person, splits by space if has multiple duties")
# print("Current question: {}".format(QUESTIONS_LIST))
#
# for ppl in ROLES_LIST:
#     __tmp = input("Duties of {}, split by space: ".format(ppl))
#     __duties = __tmp.split()
#     for __duty in __duties:
#         person[ppl].add_duty(question[__duty])


# print("Input queries of each person, splits by space if has multiple queries")
# print("Current question: {}".format(QUESTIONS_LIST))
# for __ppl in ROLES_LIST:
#     __tmp = input("queries of {}, split by space: ".format(__ppl))
#     __duties = __tmp.split()
#     for __duty in __duties:
#         person[__ppl].add_query(question[__duty])

for __ppl in ROLES_LIST:
    for __query in QUERY[__ppl]:
        person[__ppl].add_query(question[__query])

strategy = Strategy(person_list, question_list).maximized_strategy()
print(strategy)


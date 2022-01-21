
class Question:
    def __init__(self , prompt , answer):
        self.prompt = prompt
        self.answer = answer

import random
import Question


question_prompts = [
    "What is the largest country in the world?\n(1) Russia\n(2) Canada\n(3) China\n(4) United States\n",
    "Which state has the largest area?\n(1) Maharashtra\n(2) Madhya Pradesh\n(3) Uttar Pradesh\n(4) Rajasthan\n",
    "Which Which Indian personality got two oscars ?\n(1) A.R Rehman\n(2) Amitabh Bachan\n(3) Hritik Roshan\n(4) Selmon Bhoi\n"
]

questions = [
    Question(question_prompts[0] , "1"),
    Question(question_prompts[1] , "4"),
    Question(question_prompts[2] , "1"),
]

random = random.choices(questions , k=2)

def run_test(random):
    score = 0 
    for question in random:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("Your total score from 2 is :  " , score) 

    # print(random.sample(question_prompts , 2))

run_test(random)

#coding:utf-8
from typing import List
from typing import Tuple
import random
from const import *
from neural_network import NeuralNetwork

class Agent:
    def __init__(self):
        self.neural_network = NeuralNetwork()
        self.correct_answer_count = 0
        self.is_correct_history : List[bool] = []
        self.accuracy = 0.0

class Wcst:
    def __init__(self):
        self.step_counter = 0
        self.step_uppter_limit = 64
        self.rules = ['color','shape','number']
        self.current_rule = random.choice(self.rules)
        self.question_vector = []
        self.feedback_vector = []
        self.correct_answer_vector = []

    def question(self) -> Tuple[List[int],List[int]]:
        """
        return randomized question_vector and correct_answer_vector
        following the current_rule.
        """
        l = [0,1,2,3]
        color = [0,0,0,0]
        shape = [0,0,0,0]
        number = [0,0,0,0]
        self.question_vector = []
        self.correct_answer_vector = [0,0,0,0]
        correct_answer_number = l.pop(random.randint(0,len(l)-1))
        self.correct_answer_vector[correct_answer_number] = 1
        if self.current_rule == 'color':
            color[correct_answer_number] = 1
            shape[l.pop(random.randint(0,len(l)-1))] = 1
            number[l.pop(random.randint(0,len(l)-1))] = 1
        elif self.current_rule == 'shape':
            color[l.pop(random.randint(0,len(l)-1))] = 1
            shape[correct_answer_number] = 1
            number[l.pop(random.randint(0,len(l)-1))] = 1
        elif self.current_rule == 'number':
            color[l.pop(random.randint(0,len(l)-1))] = 1
            shape[l.pop(random.randint(0,len(l)-1))] = 1
            number[correct_answer_number] = 1
        self.question_vector += color
        self.question_vector += shape
        self.question_vector += number
        self.question_vector += [1,0]
        self.question_vector += [0,0]
        self.question_vector += [0,0,0,0]
        return(self.question_vector, self.correct_answer_vector)

    def feedback(self, is_correct:bool, answer_vector:List[int]) -> List[int]:
        self.feedback_vector = self.question_vector[:12]
        self.feedback_vector += [0,1]
        if is_correct == True:
            self.feedback_vector += [1,0]
        elif is_correct == False:
            self.feedback_vector += [0,1]
        self.feedback_vector += answer_vector
        return(self.feedback_vector)

    def change_rule(self):
        next_rule = random.choice(self.rules)
        while(next_rule == self.current_rule):
            next_rule = random.choice(self.rules)
        self.current_rule = next_rule

if __name__=='__main__':
    agents = [Agent() for i in range(1)]
    wcst = Wcst()

    def play(agent,wcst):
        for round_no in range(64):
            q_v, a_v = wcst.question()
            print(q_v,a_v)
            output = agent.neural_network.get_output(q_v)
            corrected_output = [0 for i in range(4)]
            corrected_output[output.index(max(output))] = 1
            if(corrected_output == a_v):
                agent.is_correct_history.append(True)
                agent.correct_answer_count += 1
            else:
                agent.is_correct_history.append(False)

    def evolution(agents):
        pass

    for generation_no in range(1):
        for agent_no in range(len(agents)):
            agent = agents[agent_no]
            play(agent,wcst)

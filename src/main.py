#coding:utf-8
import random
from const import *
from neural_network import NeuralNetwork

class Agent:
    def __init__(self):
        neural_network = NeuralNetwork()
        correct_answer_count = 0
        accuracy = 0.0

class Wcst:
    def __init__(self):
        self.step_counter = 0
        self.step_uppter_limit = 64
        self.rules = ['color','shape','number']
        self.current_rule = random.choice(self.rules)
        self.question_vector = []
        self.feedback_vector = []
        self.answer_vector = []
    def question(self):
        l = [0,1,2,3]
        color = [0,0,0,0]
        shape = [0,0,0,0]
        number = [0,0,0,0]
        correct_answer_number = l.pop(random.randint(0,len(l)-1))
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
        return(self.question_vector)
    def feedback(self):
        pass
    def change_rule(self):
        next_rule = random.choice(self.rules)
        while(next_rule == self.current_rule):
            next_rule = random.choice(self.rules)
        self.current_rule = next_rule

if __name__=='__main__':
    wcst = Wcst()
    wcst.question()
    wcst.change_rule()

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
        self.current_rule = random.choice(rules)
        self.question_vector = [0 for i in range(20)]
        self.answer_vector = [0 for i in range(4)]
    def question(self):
        pass
    def feedback(self):
        pass
    def change_rule(self):
        pass

if __name__=='__main__':

import random
from const import *

class Neuron:
    def __init__(self,neuron_id):
        #dynamic
        activation = 0.0
        #genetic
        activation_bias = random.choice([-1,0,1])
        coefficient = random.choice([1,4,9])

class Connection:
    def __init__(self):
        #dynamic
        weight = 0.0
        #genetic
        innate_weight = random.uniform(-1.0,1.0)
        input_neuron_index = random.randint(-1, H + O + i)
        neuromodulation_neuron_index
        neurotransmission_neuron_index
        output_neuron_index

class NeuralNetwork:
    def __init__(self):
        

import random
from const import *

class Neuron:
    def __init__(self):
        #dynamic
        self.activation = 0.0
        #genetic
        self.activation_bias = random.choice([-1,0,1])
        self.coefficient = random.choice([1,4,9])

class Connection:
    def __init__(self):
        #dynamic
        self.weight = 0.0
        #genetic
        self.innate_weight = random.uniform(-1.0,1.0)
        self.input_neuron_index = random.randint(0, NH+NO+NI)
        self.neuromodulation_neuron_index = random.randint(-1, NH+NO+NI)
        self.neurotransmission_neuron_index = random.randint(-1, NH+NO+NI)
        self.output_neuron_index = random.randint(0, NH+NO)

class NeuralNetwork:
    """
    - 入力に対して出力を求める
    - 重みの更新
    - 突然変異
    """
    def __init__(self):
        self.initial_connection_number = random.randint(95,105)
        self.connections = [Connection() for i in range(self.initial_connection_number)]

if __name__=='__main__':
    test_agent = NeuralNetwork()
    print(len(test_agent.connections))
    print("---")
    for i in range(len(test_agent.connections)):
        print(test_agent.connections[i].weight,\
        test_agent.connections[i].input_neuron_index,\
        test_agent.connections[i].neurotransmission_neuron_index,\
        test_agent.connections[i].output_neuron_index)

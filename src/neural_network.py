from typing import List
import random
import numpy as np
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
        self.weight = random.uniform(-1.0,1.0)
        #genetic
        self.innate_weight = self.weight
        self.input_neuron_index = random.randint(0, NH+NO+NI -1)
        self.neuromodulation_neuron_index = random.randint(-1, NH+NO+NI -1)
        self.neurotransmission_neuron_index = random.randint(-1, NH+NO+NI -1)
        self.output_neuron_index = random.randint(0, NH+NO -1)

class NeuralNetwork:
    def __init__(self):
        self.connections = [Connection() for i in range(random.randint(INITIAL_CONNECTION_NUM-5,INITIAL_CONNECTION_NUM+5))]
        self.neurons = [Neuron() for i in range(NH+NO+NI)]

    def get_activation(self,no:int) -> float:
        connection_id = []
        t_c = []
        for i in range(len(self.connections)):
            if(self.connections[i].output_neuron_index== no):
                connection_id.append(i)
                if(self.connections[i].neurotransmission_neuron_index == -1 or \
               self.neurons[self.connections[i].neurotransmission_neuron_index].activation > 0.0):
                    t_c.append(1.0)
                else:
                    t_c.append(0.0)
        if len(connection_id) == 0:
            return 0.0
        else:
            output = 0.0
            for i in range(len(connection_id)):
                cid = connection_id[i]
                output += self.connections[cid].weight * \
                    self.neurons[self.connections[cid].input_neuron_index].activation * \
                    t_c[i]
            output = np.tanh(self.neurons[no].coefficient * output + self.neurons[no].activation_bias)
            #update weights
            for i in range(len(connection_id)):
                cid = connection_id[i]
                self.connections[cid].weight += 2 * \
                    self.neurons[self.connections[cid].neuromodulation_neuron_index].activation * \
                    self.neurons[self.connections[cid].input_neuron_index].activation * \
                    t_c[i]
            return output

    def get_output(self,input_vector:List()):
        for i in range(NI):
            self.neurons[NH+NO+i].activation = input_vector[i]
        for i in range(NH+NO):
            self.neurons[i].activation = self.get_activation(i)
        output_vector = []
        for i in range(NO):
            output_vector.append(self.neurons[NH+i].activation)
        return output_vector
    def mutation(self):
        #delete and add connection randomly
        if(random.random() < 0.1 and len(self.connections) > CONNECTION_NUM_LOWER_LIMIT): #delete
            del self.connections[ random.randint(0,len(self.connections)) ]
        if(random.random() < 0.1 and len(self.connections) < CONNECTION_NUM_UPPER_LIMIT): #add
            self.connections.append(Connection())
        for i in range(len(self.neurons)):
            if(random.random() < 0.01):
                self.neurons[i] = Neuron()
        for i in range(len(self.connections)):
            if(random.random() < 0.01):
                self.connections[i] = Connection()

if __name__=='__main__':
    test_neural_network = NeuralNetwork()
    def showinfo():
        print('num_of_connection:',len(test_neural_network.connections))
        print('w      i m t o')
        for i in range(len(test_neural_network.connections)):
            print('{:.4f}'.format(test_neural_network.connections[i].weight),\
            test_neural_network.connections[i].input_neuron_index,\
            test_neural_network.connections[i].neuromodulation_neuron_index,\
            test_neural_network.connections[i].neurotransmission_neuron_index,\
            test_neural_network.connections[i].output_neuron_index)
        print('activation')
        for i in range(len(test_neural_network.neurons)):
            print('{:.4f}'.format(test_neural_network.neurons[i].activation))
    showinfo()
    test_neural_network.get_output([1.0,1.0])
    showinfo()
    test_neural_network.mutation()

#include "Random.cpp"
#include "const.cpp"
#include<iostream>

class connection
{
    private:
    float weight;
    float innate_weight;
    int input_neuron_index;
    int neuromodulation_neuron_index;
    int neurotransmission_neuron_index;
    int output_neuron_index;

    public:
    connection()
    {
        innate_weight = rnd(-100000, 100000) / 100000.0;
        weight = innate_weight;
        input_neuron_index = rnd(0, NH+NO+NI-1);
        neuromodulation_neuron_index = rnd(-1, NH+NO+NI-1);
        neurotransmission_neuron_index = rnd(-1, NH+NO+NI-1);
        output_neuron_index = rnd(0, NH+NO-1);
    }

    void show_members()
    {
        std::cout << innate_weight <<","<< weight <<","<< input_neuron_index <<","<< neuromodulation_neuron_index <<","<< neurotransmission_neuron_index <<","<< output_neuron_index <<","<< std::endl;
    }

};

int main()
{
    connection clist[10];
    for(int i=0;i<10;i++)
    {
        clist[i].show_members();
    }

    return 0;
}

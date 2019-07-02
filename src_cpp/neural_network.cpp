#include "Random.cpp"
#include<iostream>

class neuron
{
    private:
    float activation_val = 0.0; // -1.0 ~ +1.0
    int activation_bias;
    int coefficient;

    public:
    neuron()
    {
        int flag = rnd(3);
        if(flag == 0){ activation_bias = -1; }
        else if (flag == 1){ activation_bias = 0; }
        else { activation_bias = 1; }

        flag = rnd(3);
        if(flag == 0){ coefficient = 1; }
        else if (flag == 1){ coefficient = 4; }
        else { coefficient = 9; }
    }
};

int main()
{
    neuron n[10];
    for(int i=0;i<10;i++)
    {
        std::cout << n[i].activation_val << std::endl;
        std::cout << n[i].activation_bias << std::endl;
    }

    return 0;
}

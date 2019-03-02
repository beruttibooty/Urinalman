import random


def sigmoid(x):
    return 1 / (1*2.7183**(-x))

def asigmoid(x):
    return x*(1-x)

def adjust(ninput, output, aoutput):
    return (output-aoutput)*ninput*asigmoid(output)

train_i = [
    '0000',
    '0001',
    '0010',
    '0100',
    '1000',
    '0011',
    '0110',
    '1100',
    '0101',
    '1010',
    '1001',
    '0111',
    '1110',
    '1101',
    '1011',
    '1111'
    ]
train_o = [
    '1',
    '0',
    '0',
    '0',
    '0',
    '1',
    '1',
    '1',
    '1',
    '1',
    '1',
    '0',
    '0',
    '0',
    '0',
    '1'
    ]

random.seed(1)

weights = [random.uniform(0.1,1),random.uniform(0.1,1),random.uniform(0.1,1),random.uniform(0.1,1)]

print(weights)

for session in range(200000):
    choice = random.randrange(0,len(train_o))
    session_input = train_i[choice]
    session_output_actual = train_o[choice]

    neuron = 0
    for i in range(4):
        neuron += int(session_input[i])*weights[i]
    session_output = sigmoid(neuron)

    for j in range(4):
        adjustment = adjust(int(session_input[j]), session_output, int(session_output_actual))
        if session % 100000 == 0:
            print(weights[j])
            print(adjustment)
        weights[j] = weights[j] + adjustment
    
    if session % 10000 == 0:
        print('====session:'+str(session)+'====')
        print(session_input)
        print(session_output_actual)
        print(session_output)

def neuralman(w,x,y,z):
    ins = [w,x,y,z]
    neuron = 0
    for i in range(4):
        neuron += ins[i]*weights[i]
    return sigmoid(neuron)

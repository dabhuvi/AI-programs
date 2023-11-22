import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def initialize_weights(input_size, hidden_size, output_size):
    
    weights_input_hidden = np.random.rand(input_size, hidden_size)
    bias_hidden = np.zeros((1, hidden_size))
    weights_hidden_output = np.random.rand(hidden_size, output_size)
    bias_output = np.zeros((1, output_size))

    return weights_input_hidden, bias_hidden, weights_hidden_output, bias_output

def forward_pass(inputs, weights_input_hidden, bias_hidden, weights_hidden_output, bias_output):
    
    hidden_layer_output = sigmoid(np.dot(inputs, weights_input_hidden) + bias_hidden)
    output_layer_output = sigmoid(np.dot(hidden_layer_output, weights_hidden_output) + bias_output)

    return hidden_layer_output, output_layer_output

def train_network(inputs, targets, learning_rate, epochs):
    input_size = inputs.shape[1]
    hidden_size = 4 
    output_size = targets.shape[1]

    weights_input_hidden, bias_hidden, weights_hidden_output, bias_output = initialize_weights(
        input_size, hidden_size, output_size)

    for epoch in range(epochs):
        
        hidden_output, network_output = forward_pass(
            inputs, weights_input_hidden, bias_hidden, weights_hidden_output, bias_output)
        error = targets - network_output
        output_delta = error * sigmoid_derivative(network_output)
        hidden_error = output_delta.dot(weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(hidden_output)

        weights_hidden_output += hidden_output.T.dot(output_delta) * learning_rate
        bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
        weights_input_hidden += inputs.T.dot(hidden_delta) * learning_rate
        bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

    return weights_input_hidden, bias_hidden, weights_hidden_output, bias_output

training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
training_targets = np.array([[0], [1], [1], [0]])

learned_weights_input_hidden, learned_bias_hidden, learned_weights_hidden_output, learned_bias_output = \
    train_network(training_inputs, training_targets, learning_rate=0.1, epochs=10000)

test_input = np.array([[0, 0]])
_, predicted_output = forward_pass(
    test_input, learned_weights_input_hidden, learned_bias_hidden, learned_weights_hidden_output, learned_bias_output)

print("Predicted Output:", predicted_output)

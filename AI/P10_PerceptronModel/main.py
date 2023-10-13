import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_and_process_data() -> np.matrix:
    import pathlib
    df = pd.read_csv((str(pathlib.Path(__file__).parent.absolute()) + '/iris.csv'), header=None)
    df[4] = np.where(df[4] == 'Iris-setosa', 0, 1)
    return np.asmatrix(df, dtype='float64')

data = load_and_process_data()

training_data = np.concatenate((data[:45, :], data[50:95, :]), axis=0)
test_data = np.concatenate((data[45:50, :], data[95:100, :]), axis=0)
benchmark = np.concatenate((data[49, :], data[99, :]), axis=0)

class Perceptron:    
    def __init__(self, learning_rate: float = 0.1, inputs: int = 4, output_index = 4):
        self.learning_rate = learning_rate
        self.weights = tuple([0 for _ in range(inputs)])
        self.bias = 0
        self.output_index = output_index
        
    def activation(self, values) -> int:
        return 1 if sum([w * v for w, v in zip(self.weights, values)]) + self.bias > 0 else 0
    
    def train(self, data, benchmark = None, epochs: int = 5):
        for i in range(epochs):
            for d in data:
                values = d.tolist()[0]
                prediction = self.activation(values[:self.output_index])
                error = values[self.output_index] - prediction
                self.weights = tuple([w + self.learning_rate * error * v for w, v in zip(self.weights, values[:self.output_index])])
                self.bias += self.learning_rate * error
            
            if benchmark is not None:
                print(F"Epoch: {i}\n----------")
                print('Weights: ', end="")
                print(["{:.2f}".format(w) for w in self.weights])
                print(f"Bias: {self.bias}")
                for j, _b in enumerate(benchmark):
                    b = _b.tolist()[0]
                    prediction = self.activation(b[:self.output_index])
                    error = b[self.output_index] - prediction
                    print(f'Benchmark: {j} | Predicted: {prediction} | Actual: {b[4]} | Error: {error}')
                print("---x---x---x---x---x---x---x---x---x---x---")
    
    def test(self, data):
        for _d in data:
            d = _d.tolist()[0]
            print(f'Predicted: {self.activation(d[:self.output_index])} | Actual: {d[self.output_index]}')
    

perceptron = Perceptron()
print("[] Training Perceptron")
perceptron.train(training_data, benchmark)
print("[] Test cases: ")
perceptron.test(test_data)

#   x-y     sepal width            petal length
plt.scatter(np.array(data[:50, 1]), np.array(data[:50, 2]), marker='o', label='setosa')
plt.scatter(np.array(data[50:, 1]), np.array(data[50:, 2]), marker='x', label='versicolor')
plt.xlabel('sepal width')
plt.ylabel('petal length')

slope = (-(perceptron.bias)/(perceptron.weights[2])) / ((perceptron.bias)/(perceptron.weights[1]))
plt.plot([2, 5], (slope * np.array([2, 5])) + (-perceptron.bias / perceptron.weights[2]), label='Decision Boundary', color='red')
plt.legend()
plt.show()
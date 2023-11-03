from math import tanh

class Perceptron:
    def __init__(self, learning_rate = 0.05, num_inputs = 4):
        self.learning_rate = learning_rate
        self.weights = [0 for _ in range(num_inputs)]
        self.bias = 0
        
    def activation(self, input_vector):
        # return 1 if sum([w * v for w, v in zip(self.weights, input_vector)]) + self.bias > 0 else -1
        return tanh(sum([w * v for w, v in zip(self.weights, input_vector)]) + self.bias)
    
    def train(self, data, epochs = 1000):
        for _ in range(epochs):
            for dp in data:
                prediction = self.activation(dp[:4])
                loss = dp[4] - prediction
                self.weights = [w + self.learning_rate * loss * v for w, v in zip(self.weights, dp[:4])]
                self.bias += self.learning_rate * loss
                
                

def main():
    
    from pathlib import Path
    script_dir = Path(__file__).parent.absolute()
    
    
    with open(script_dir / "iris.csv", "r") as f:
        data = f.readlines()
        data = [d.replace("Iris-setosa", "-1").replace("Iris-versicolor", "1") for d in data]
        data = [d.strip().split(",") for d in data]
        data = [[float(v) for v in d] for d in data]
        
    perceptron = Perceptron()
    
    test_set = data[45:50] + data[95:100]
    training_set = data[:45] + data[50:95]
    
    perceptron.train(training_set)
    
    print(f"Trained Weights: {perceptron.weights} | Bias: {perceptron.bias}")
    
    print("Test Set: ")
    for dp in test_set:
        prediction = perceptron.activation(dp[:4])
        print(f"Predicted: {prediction} | Actual: {dp[4]}")
    
    import matplotlib.pyplot as plt
    
    feat_a, feat_b = 1, 2
    
    feat_a = perceptron.weights.index(max(perceptron.weights))
    feat_b = perceptron.weights.index(min(perceptron.weights))
    
    print(f"Using features {feat_a} and {feat_b}")
    
    plt.scatter([d[feat_b] for d in data[:50]], [d[feat_a] for d in data[:50]], color="red", label="Iris-setosa")
    plt.scatter([d[feat_b] for d in data[50:100]], [d[feat_a] for d in data[50:100]], color="blue", label="Iris-versicolor")
    
    plt.xlabel("Sepal Width")
    plt.ylabel("Petal Length")
    
    min_x = min(x[feat_b] for x in data[:50] + data[50:100]) - 0.1
    max_x = max(x[feat_b] for x in data[:50] + data[50:100]) + 0.1
    
    slope = (-(perceptron.bias)/(perceptron.weights[2])) / ((perceptron.bias)/(perceptron.weights[1]))
    plt.plot([min_x, max_x], [slope * w + (-perceptron.bias / perceptron.weights[2]) for w in [min_x, max_x]], label='Decision Boundary', color='black')
    plt.fill_between([min_x, max_x], [slope * w + (-perceptron.bias / perceptron.weights[2]) for w in [min_x, max_x]], 0, color="red", alpha=0.1)
    plt.fill_between([min_x, max_x], [slope * w + (-perceptron.bias / perceptron.weights[2]) for w in [min_x, max_x]], 6, color="blue", alpha=0.1)
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    main()
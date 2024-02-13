# P10_PerceptronModel

## References 

- <https://towardsdatascience.com/perceptron-and-its-implementation-in-python-f87d6c7aa428>
- <https://www.kaggle.com/datasets/uciml/iris> -- We will only use the first 2 categories of this dataset, the last one is not linearly separable and cannot be classified using a single layer perceptron.
- <https://www.codecademy.com/learn/perceptrons-and-neural-nets-skill-path/modules/perceptrons-skill-path/cheatsheet>
- [main.noexternal.py](./main.noexternal.py)

```csv
SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species
```

## Theory


**Title: Implementing Perceptron Model on the Iris Dataset**

**Objective:**
The objective of this practical is to implement a perceptron model and apply it to the Iris Dataset for binary classification. The task involves using only the first 100 rows of the dataset to simplify the problem into a binary classification scenario.

**Background:**
The perceptron is the simplest form of a neural network, capable of binary classification. It takes multiple inputs, each associated with a weight, and produces a real-valued output. Mathematically, the output $y$ is determined by applying weights $w_i$ to the input features $x_i$, summing them up, and passing the result through an activation function. The perceptron model can handle both binary and real-valued inputs and outputs.

The core idea behind the perceptron is to learn a decision boundary that separates different classes in the input space. This is achieved through a learning algorithm that adjusts the weights based on the error in classification. The learning algorithm involves updating the weights using a formula that takes into account the difference between the true class label $y_{\text{true}}$ and the predicted class label $y_{\text{predicted}}$, multiplied by the input features.

**Perceptron Model:**
The perceptron model can be represented as follows:
$$ y = \begin{cases} 1 & \text{if } \sum_{i=1}^{n} w_i \cdot x_i + b > 0 \\ 0 & \text{otherwise} \end{cases} $$

where:
- $y$ is the output.
- $w_i$ is the weight associated with input $x_i$.
- $b$ is the bias term.

**Learning Algorithm:**
The learning algorithm for the perceptron involves adjusting weights based on the error in the classification. The weight update rule is given by:
$$ w_i^{new} = w_i^{old} + \alpha \cdot (y_{\text{true}} - y_{\text{predicted}}) \cdot x_i $$

where:
- $\alpha$ is the learning rate.
- $y_{\text{true}}$ is the true class label.
- $y_{\text{predicted}}$ is the predicted class label.

**Iris Dataset:**
The Iris Dataset consists of 150 samples of iris flowers, each belonging to one of three species: setosa, versicolor, or virginica. For this practical, we focus on a binary classification problem by using only the first 100 rows, considering two classes - setosa (class 0) and versicolor (class 1).

**Procedure:**
1. Load the Iris Dataset and extract the first 100 rows.
2. Preprocess the data by encoding the class labels (setosa as 0, versicolor as 1).
3. Initialize weights and bias for the perceptron model.
4. Implement the perceptron learning algorithm.
5. Train the perceptron on the preprocessed data.
6. Evaluate the model's performance using metrics such as accuracy.

**Conclusion:**
This practical introduces the foundational concept of a perceptron model and its application to a real-world dataset. By implementing the perceptron learning algorithm on the Iris Dataset, you gain insights into the fundamental principles of binary classification in the context of artificial intelligence.

---

## Files

- [main.noexternal.py](./main.noexternal.py) - without external libraries
- [main.py](./main.py) - with numpy and pandas
- [iris.csv](./iris.csv) - Place next to script
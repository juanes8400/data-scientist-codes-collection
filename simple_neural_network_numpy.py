"""
Simple Neural Network with Numpy.

Neural networks were pioneered by Warren McCulloch and Walter Pitts in
the 1940s and later popularised by researchers like Geoffrey Hinton.
This script implements a minimal two-layer neural network using only
NumPy to solve the XOR problem.
"""

import numpy as np

# XOR input and output
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Network architecture
np.random.seed(42)
W1 = np.random.randn(2, 2)
b1 = np.zeros((1, 2))
W2 = np.random.randn(2, 1)
b2 = np.zeros((1, 1))

# Activation functions
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(a):
    return a * (1 - a)

# Training via gradient descent
lr = 0.1
for epoch in range(10000):
    # Forward pass
    z1 = X.dot(W1) + b1
    a1 = sigmoid(z1)
    z2 = a1.dot(W2) + b2
    a2 = sigmoid(z2)

    # Backward pass
    dz2 = a2 - y
    dW2 = a1.T.dot(dz2)
    db2 = np.sum(dz2, axis=0, keepdims=True)

    dz1 = dz2.dot(W2.T) * sigmoid_derivative(a1)
    dW1 = X.T.dot(dz1)
    db1 = np.sum(dz1, axis=0, keepdims=True)

    # Parameter update
    W2 -= lr * dW2
    b2 -= lr * db2
    W1 -= lr * dW1
    b1 -= lr * db1

# Predict
preds = (a2 > 0.5).astype(int)
print("Predictions after training:", preds.ravel())

"""
Decision Tree Regressor.

Decision trees can also be used for regression by predicting the mean
target value in each terminal node. We fit a regression tree to
synthetic data generated from a sine function.
"""

import numpy as np
from sklearn.tree import DecisionTreeRegressor

rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()

model = DecisionTreeRegressor(random_state=0)
model.fit(X, y)

print("Predicted value for 2.5:", model.predict([[2.5]])[0])

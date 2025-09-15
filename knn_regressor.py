"""
kNN Regressor.

kNN can be used for regression by averaging the target values of the
nearest neighbours. We fit a kNN regressor to synthetic data from a
sine function.
"""

import numpy as np
from sklearn.neighbors import KNeighborsRegressor

rng = np.random.RandomState(0)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()

model = KNeighborsRegressor(n_neighbors=5)
model.fit(X, y)

print("Predicted value for 2.5:", model.predict([[2.5]])[0])

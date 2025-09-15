"""
Gradient Boosting Regressor.

This example fits a gradient boosting regressor to synthetic sine
data and predicts the value at 2.5.
"""

import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()

model = GradientBoostingRegressor(random_state=0)
model.fit(X, y)

print("Predicted value for 2.5:", model.predict([[2.5]])[0])

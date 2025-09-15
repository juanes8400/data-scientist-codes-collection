"""
Lasso LARS Regression.

Least Angle Regression (LARS) is an efficient algorithm for fitting
Lasso models. This script demonstrates LassoLars on synthetic data.
"""

import numpy as np
from sklearn.linear_model import LassoLars

rng = np.random.RandomState(0)
X = rng.randn(100, 5)
coef = np.array([1.5, 0, -3.0, 0, 2.0])
y = X @ coef + rng.randn(100) * 0.1

model = LassoLars(alpha=0.1)
model.fit(X, y)

print("True coefficients:", coef)
print("Estimated coefficients:", model.coef_)

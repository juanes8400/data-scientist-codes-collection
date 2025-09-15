"""
Linear Regression.

Simple linear regression models the relationship between a scalar
dependent variable and one or more explanatory variables. It dates back
to the work of Gauss and Legendre. This script fits a linear model to
synthetically generated data.
"""

import numpy as np
from sklearn.linear_model import LinearRegression

# Generate synthetic data
rng = np.random.RandomState(42)
X = 2 * rng.rand(100, 1)
y = 4 + 3 * X[:, 0] + rng.randn(100)

model = LinearRegression()
model.fit(X, y)

print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

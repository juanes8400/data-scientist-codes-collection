"""
Polynomial Regression.

By augmenting features with polynomial terms, linear models can
approximate non-linear relationships. This example uses a second
order polynomial to fit synthetic data generated from a quadratic
function.
"""

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

rng = np.random.RandomState(0)
X = 2 * rng.rand(100, 1) - 1
y = 1 + 2 * X[:, 0] + 3 * X[:, 0] ** 2 + rng.randn(100) * 0.1

poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)
model = LinearRegression()
model.fit(X_poly, y)

print("Learned coefficients:", model.coef_)
print("Intercept:", model.intercept_)

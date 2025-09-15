"""
Ridge Regression.

Ridge regression, proposed by Hoerl and Kennard in 1970, adds an L2
penalty to linear regression to reduce overfitting. This example
demonstrates ridge regression on synthetic data.
"""

import numpy as np
from sklearn.linear_model import Ridge

rng = np.random.RandomState(0)
X = 2 * rng.rand(100, 1)
y = 4 + 3 * X[:, 0] + rng.randn(100)

model = Ridge(alpha=1.0)
model.fit(X, y)

print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

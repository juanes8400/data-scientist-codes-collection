"""
Lasso Regression.

The Lasso (Least Absolute Shrinkage and Selection Operator) was
introduced by Robert Tibshirani in 1996. It adds an L1 penalty to
encourage sparse coefficients. We fit a Lasso model to synthetic data
and display the learned coefficients.
"""

import numpy as np
from sklearn.linear_model import Lasso

rng = np.random.RandomState(0)
X = rng.randn(100, 5)
coef = np.array([1.5, 0, -3.0, 0, 2.0])
y = X @ coef + rng.randn(100) * 0.1

model = Lasso(alpha=0.1)
model.fit(X, y)

print("True coefficients:", coef)
print("Estimated coefficients:", model.coef_)

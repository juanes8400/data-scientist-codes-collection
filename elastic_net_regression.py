"""
Elastic Net Regression.

Elastic net, proposed by Zou and Hastie in 2005, combines L1 and L2
regularisation. It can select variables like the Lasso while
maintaining stability like ridge. Here we fit an elastic net model
to synthetic data.
"""

import numpy as np
from sklearn.linear_model import ElasticNet

rng = np.random.RandomState(0)
X = rng.randn(100, 5)
true_coef = np.array([1.5, 0, -3.0, 0, 2.0])
y = X @ true_coef + rng.randn(100) * 0.1

model = ElasticNet(alpha=0.1, l1_ratio=0.5)
model.fit(X, y)

print("True coefficients:", true_coef)
print("Estimated coefficients:", model.coef_)

"""
Robust Regression via RANSAC.

The Random Sample Consensus (RANSAC) algorithm, introduced by Fischler
and Bolles in 1981, is robust against outliers. We generate linear
data with outliers and fit a RANSAC regressor.
"""

import numpy as np
from sklearn.linear_model import RANSACRegressor, LinearRegression

rng = np.random.RandomState(0)
# Generate inlier data
X = rng.rand(100, 1)
y = 0.5 * X[:, 0] + 0.2 + rng.randn(100) * 0.02
# Add outliers
X_outliers = rng.rand(20, 1)
y_outliers = rng.rand(20) + 2
X_full = np.vstack((X, X_outliers))
y_full = np.concatenate((y, y_outliers))

model = RANSACRegressor(base_estimator=LinearRegression())
model.fit(X_full, y_full)

print("Estimated slope:", model.estimator_.coef_[0])
print("Estimated intercept:", model.estimator_.intercept_)

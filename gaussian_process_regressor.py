"""
Gaussian Process Regression.

Gaussian processes, with roots in the work of Carl Friedrich Gauss,
provide a nonparametric Bayesian approach to regression. We fit a
GaussianProcessRegressor to synthetic data and output the predicted
mean and standard deviation for a test point.
"""

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

rng = np.random.RandomState(1)
X = np.atleast_2d(np.linspace(0, 5, 10)).T
y = np.sin(X).ravel()

# Kernel: constant * RBF
kernel = C(1.0, (1e-3, 1e3)) * RBF(1.0, (1e-2, 1e2))
gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9)
gp.fit(X, y)

y_pred, sigma = gp.predict([[2.5]], return_std=True)
print("Predicted mean:", y_pred[0])
print("Predicted std:", sigma[0])

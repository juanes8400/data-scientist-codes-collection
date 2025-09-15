"""
Support Vector Regression (SVR).

SVR extends support vector machines to regression. We fit an SVR
model with an RBF kernel to synthetic sine data and predict the
value at 2.5.
"""

import numpy as np
from sklearn.svm import SVR

rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()

model = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
model.fit(X, y)

print("Predicted value for 2.5:", model.predict([[2.5]])[0])

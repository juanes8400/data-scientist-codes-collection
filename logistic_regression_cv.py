"""
Logistic Regression with Built-in Cross-Validation.

The LogisticRegressionCV estimator performs cross-validation to
automatically select regularisation strength. We apply it to the
Iris dataset.
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegressionCV

X, y = load_iris(return_X_y=True)

model = LogisticRegressionCV(cv=5, max_iter=200)
model.fit(X, y)

print("Best C values:", model.C_)
print("Model accuracy:", model.score(X, y))

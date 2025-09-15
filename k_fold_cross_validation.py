"""
k-Fold Cross-Validation.

Cross-validation, systematically proposed by Stone and Geisser in the
1970s, assesses the performance of predictive models by dividing
the data into k subsets. This script computes the mean accuracy of
a logistic regression classifier across five folds of the Iris dataset.
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

X, y = load_iris(return_X_y=True)
model = LogisticRegression(max_iter=200)
scores = cross_val_score(model, X, y, cv=5)

print("Cross-validation scores:", scores)
print("Mean accuracy:", scores.mean())

"""
Grid Search for Hyperparameter Tuning.

GridSearchCV exhaustively searches over specified hyperparameter
values. We tune the C and gamma parameters of an SVM on the Iris
dataset using cross-validation.
"""

from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

X, y = load_iris(return_X_y=True)
param_grid = {'C': [0.1, 1, 10], 'gamma': ['scale', 'auto']}

grid = GridSearchCV(SVC(kernel='rbf'), param_grid, cv=3)
grid.fit(X, y)

print("Best parameters:", grid.best_params_)
print("Best cross-validated score:", grid.best_score_)

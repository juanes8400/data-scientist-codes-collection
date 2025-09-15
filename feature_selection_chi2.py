"""
Feature Selection using Chi-Squared Test.

Chi-squared statistics can be used to select the most informative
categorical features relative to the target variable. In this demo,
we compute the chi² scores for the Iris dataset and retain the top
two features.
"""

from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, chi2

X, y = load_iris(return_X_y=True)

selector = SelectKBest(chi2, k=2)
X_new = selector.fit_transform(X, y)

print("Selected feature indices:", selector.get_support(indices=True))
print("Transformed shape:", X_new.shape)

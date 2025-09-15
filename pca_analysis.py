"""
Principal Component Analysis (PCA).

PCA was introduced by Karl Pearson in 1901 and further developed by
Harold Hotelling. It reduces the dimensionality of a dataset by
projecting it onto its principal axes. This script performs PCA on
the Iris dataset and prints the explained variance ratios.
"""

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

X, _ = load_iris(return_X_y=True)

pca = PCA(n_components=2)
pca.fit(X)

print("Explained variance ratios:", pca.explained_variance_ratio_)

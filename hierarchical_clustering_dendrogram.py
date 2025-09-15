"""
Hierarchical Clustering Dendrogram.

The dendrogram visualises the hierarchy of clusters formed by
agglomerative clustering. We compute a linkage matrix using
SciPy's Ward method and print the first five linkage rows.
"""

from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import linkage

X, _ = load_iris(return_X_y=True)

Z = linkage(X, method='ward')

print("First five linkage rows:\n", Z[:5])

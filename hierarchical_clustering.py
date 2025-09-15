"""
Agglomerative Hierarchical Clustering.

Agglomerative clustering builds nested clusters by repeatedly merging
pairs of clusters. Ward's method (1963) minimises the variance
within each cluster. In this example, we cluster the Iris dataset
hierarchically and print the assigned cluster labels for the first
10 samples.
"""

from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering

X, _ = load_iris(return_X_y=True)

model = AgglomerativeClustering(n_clusters=3, linkage='ward')
labels = model.fit_predict(X)

print("First 10 cluster labels:", labels[:10])

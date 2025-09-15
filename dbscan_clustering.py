"""
DBSCAN Clustering.

Density-Based Spatial Clustering of Applications with Noise (DBSCAN),
introduced by Ester et al. in 1996, groups together points that are
closely packed while marking outliers as noise. We apply DBSCAN to
the Iris dataset and print the cluster labels.
"""

from sklearn.datasets import load_iris
from sklearn.cluster import DBSCAN

X, _ = load_iris(return_X_y=True)

model = DBSCAN(eps=0.5, min_samples=5)
labels = model.fit_predict(X)

print("DBSCAN labels (first 20):", labels[:20])

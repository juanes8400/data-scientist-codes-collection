"""
k-Means Clustering.

k-Means is an unsupervised clustering algorithm formalised by
James MacQueen in 1967. It partitions observations into k clusters
such that each sample belongs to the cluster with the nearest mean.
Here we cluster the Iris dataset into three groups and report the
cluster centres.
"""

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

X, _ = load_iris(return_X_y=True)

model = KMeans(n_clusters=3, random_state=42)
model.fit(X)

print("Cluster centers:\n", model.cluster_centers_)

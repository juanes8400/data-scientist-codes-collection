"""
k-Means Elbow Method.

The elbow method helps determine an appropriate number of clusters by
plotting the sum of squared distances (inertia) for different k.
Here we compute inertias for k from 1 to 10 on the Iris dataset.
"""

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

X, _ = load_iris(return_X_y=True)

inertias = []
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X)
    inertias.append(model.inertia_)

for k, inertia in enumerate(inertias, start=1):
    print(f"k={k}, inertia={inertia:.2f}")

"""
t-SNE Dimensionality Reduction.

t-Distributed Stochastic Neighbor Embedding (t-SNE) was developed by
Laurens van der Maaten and Geoffrey Hinton. It projects high-dimensional
data into a lower dimensional space while preserving local structure.
This example embeds the Iris dataset into two dimensions and prints
the shape of the transformed data.
"""

from sklearn.datasets import load_iris
from sklearn.manifold import TSNE

X, _ = load_iris(return_X_y=True)

tsne = TSNE(n_components=2, random_state=42)
X_embedded = tsne.fit_transform(X)

print("t-SNE embedded shape:", X_embedded.shape)

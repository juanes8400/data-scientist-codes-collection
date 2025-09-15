"""
Gaussian Mixture Model (GMM).

GMMs, attributed to Carl Friedrich Gauss's work on normal distributions
and later elaborated by many, model data as a mixture of Gaussian
components. This example fits a GMM with three components to the Iris
dataset and prints the predicted cluster labels for the first ten
samples.
"""

from sklearn.datasets import load_iris
from sklearn.mixture import GaussianMixture

X, _ = load_iris(return_X_y=True)

model = GaussianMixture(n_components=3, random_state=42)
model.fit(X)
labels = model.predict(X)

print("GMM labels (first 10):", labels[:10])

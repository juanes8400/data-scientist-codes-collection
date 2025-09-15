"""
PCA vs LDA Comparison.

Both PCA and LDA reduce dimensionality but with different objectives:
PCA maximises variance while LDA maximises class separability. We
project the Iris dataset using both methods and report the shape of
the transformed data.
"""

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

X, y = load_iris(return_X_y=True)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

lda = LDA(n_components=2)
X_lda = lda.fit_transform(X, y)

print("PCA transformed shape:", X_pca.shape)
print("LDA transformed shape:", X_lda.shape)

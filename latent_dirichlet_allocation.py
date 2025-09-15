"""
Latent Dirichlet Allocation (LDA) for Topic Modelling.

LDA, introduced by David Blei, Andrew Ng and Michael Jordan, is a
generative probabilistic model for collections of discrete data such
as text. In this example, we create a toy document-term matrix and
fit an LDA model with two topics.
"""

import numpy as np
from sklearn.decomposition import LatentDirichletAllocation

# Toy document-term matrix (5 documents, 6 words)
X = np.array([
    [1, 2, 0, 0, 3, 1],
    [0, 0, 1, 3, 0, 2],
    [2, 1, 0, 1, 0, 0],
    [0, 1, 3, 2, 0, 0],
    [3, 0, 0, 0, 2, 1],
])

model = LatentDirichletAllocation(n_components=2, random_state=0)
model.fit(X)

print("Topic distributions for first document:", model.transform(X)[0])

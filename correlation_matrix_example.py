"""
Correlation Matrix Example.

Correlation matrices quantify linear relationships among features. We
compute the Pearson correlation matrix for the Iris dataset and
display the first few rows.
"""

import pandas as pd
from sklearn.datasets import load_iris

data = load_iris(as_frame=True)
df = data.frame

corr_matrix = df.corr(numeric_only=True)
print("Correlation matrix:\n", corr_matrix.head())

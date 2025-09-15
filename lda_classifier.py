"""
Linear Discriminant Analysis (LDA) Classifier.

LDA, formulated by Ronald A. Fisher in 1936, finds linear combinations
of features that maximise class separability. Here we fit an LDA
classifier to the Iris dataset and report its accuracy.
"""

from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LinearDiscriminantAnalysis()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("LDA accuracy:", accuracy_score(y_test, y_pred))

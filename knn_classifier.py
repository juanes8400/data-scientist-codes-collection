"""
k-Nearest Neighbours (kNN) Classifier.

The kNN algorithm was introduced by Evelyn Fix and Joseph Hodges in 1951.
It classifies observations by majority vote among the k closest samples.
This example trains a kNN classifier on the Iris dataset and reports the
classification accuracy.
"""

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("kNN accuracy:", accuracy_score(y_test, y_pred))

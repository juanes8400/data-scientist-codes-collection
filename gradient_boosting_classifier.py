"""
Gradient Boosting Classifier.

Gradient boosting was developed by Jerome Friedman in the late 1990s.
It builds an ensemble of weak learners sequentially, each correcting
the mistakes of its predecessor. We train a gradient boosting
classifier on the Iris dataset and display its accuracy.
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = GradientBoostingClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Gradient Boosting accuracy:", accuracy_score(y_test, y_pred))

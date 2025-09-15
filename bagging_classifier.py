"""
Bagging Classifier.

Bootstrap aggregating (bagging), proposed by Breiman in 1996,
reduces variance by combining models trained on bootstrap samples.
We fit a bagging classifier on the Iris dataset.
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

base = DecisionTreeClassifier()
model = BaggingClassifier(base_estimator=base, n_estimators=50, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Bagging accuracy:", accuracy_score(y_test, y_pred))

"""
Decision Tree Classifier.

Decision trees, popularised by Ross Quinlan in the 1980s, recursively
partition the feature space based on attribute values. Here we train
a decision tree on the Iris dataset and evaluate its accuracy on a
hold-out test set.
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Decision Tree accuracy:", accuracy_score(y_test, y_pred))

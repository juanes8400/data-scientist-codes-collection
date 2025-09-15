"""
Random Forest Classifier.

Random forests were introduced by Leo Breiman in 2001. They combine
multiple decision trees using bagging and random feature selection to
improve generalisation. This script fits a random forest to the Iris
dataset and reports its accuracy.
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Random Forest accuracy:", accuracy_score(y_test, y_pred))

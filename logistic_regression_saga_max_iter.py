"""
Logistic Regression Using SAGA Solver with Increased Iterations.

The saga solver supports L1, L2 and elastic net penalties and scales
well to large datasets. This script trains a logistic regression
model with saga on the Iris dataset with a high iteration limit.
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LogisticRegression(solver='saga', max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Logistic Regression (saga) accuracy:", accuracy_score(y_test, y_pred))

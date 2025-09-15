"""
Logistic Regression with Regularisation.

Regularisation controls model complexity. We compare L1 and L2
penalties on the Iris dataset using scikit-learn's LogisticRegression
with different penalty arguments.
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# L2 penalty
model_l2 = LogisticRegression(penalty='l2', solver='lbfgs', max_iter=200)
model_l2.fit(X_train, y_train)
y_pred_l2 = model_l2.predict(X_test)

# L1 penalty using saga solver
model_l1 = LogisticRegression(penalty='l1', solver='saga', max_iter=200)
model_l1.fit(X_train, y_train)
y_pred_l1 = model_l1.predict(X_test)

print("L2 penalty accuracy:", accuracy_score(y_test, y_pred_l2))
print("L1 penalty accuracy:", accuracy_score(y_test, y_pred_l1))

"""
Logistic Regression Classifier on the Iris dataset.

Logistic regression, popularized by statistician David Cox in 1958,
models the probability of class membership using the logistic function.
Here we demonstrate a simple binary classification on two classes from
the Iris dataset.
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the iris dataset and restrict to two classes (setosa and versicolor)
X, y = load_iris(return_X_y=True)
mask = y < 2
X = X[mask]
y = y[mask]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Fit logistic regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate accuracy
print("Logistic Regression accuracy:", accuracy_score(y_test, y_pred))

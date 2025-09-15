"""
Gaussian Naive Bayes Classifier.

Naive Bayes classifiers, based on Bayes' theorem formulated by
Reverend Thomas Bayes in the 18th century, assume feature independence.
This example fits a Gaussian Naive Bayes classifier to the Iris dataset
and outputs the accuracy.
"""

from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Gaussian Naive Bayes accuracy:", accuracy_score(y_test, y_pred))

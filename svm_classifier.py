"""
Support Vector Machine (SVM) Classifier.

Support vector machines were developed by Vladimir Vapnik and
Alexey Chervonenkis. They find a hyperplane that maximises the margin
between classes. This example applies an SVM with a radial basis
function kernel to the Iris dataset.
"""

from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = SVC(kernel='rbf', gamma='scale')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("SVM accuracy:", accuracy_score(y_test, y_pred))

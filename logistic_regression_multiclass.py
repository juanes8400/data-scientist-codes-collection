"""
Multiclass Logistic Regression.

We train a multinomial logistic regression model on the digits
dataset, which contains ten classes (0-9). The model uses the
saga solver to handle the multinomial objective.
"""

from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LogisticRegression(multi_class='multinomial', solver='saga', max_iter=100)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Multiclass logistic regression accuracy:", accuracy_score(y_test, y_pred))

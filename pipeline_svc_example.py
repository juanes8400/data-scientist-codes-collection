"""
Pipeline Example with Standard Scaler and SVC.

Pipelines, advocated by many practitioners, help chain preprocessing
and modelling steps. We build a pipeline that standardises features
and then fits an SVM classifier.
"""

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svc', SVC(kernel='rbf'))
])
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print("Pipeline SVC accuracy:", accuracy_score(y_test, y_pred))

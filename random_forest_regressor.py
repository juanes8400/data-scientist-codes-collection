"""
Random Forest Regressor.

Similar to its classification counterpart, the random forest
regressor averages predictions from multiple decision trees. We
demonstrate on synthetic sine data.
"""

import numpy as np
from sklearn.ensemble import RandomForestRegressor

rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()

model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(X, y)

print("Predicted value for 2.5:", model.predict([[2.5]])[0])

"""
Seasonal Decomposition of Time Series.

Seasonal decomposition separates a time series into trend, seasonal
and residual components. We generate a sine wave with noise and
use statsmodels' seasonal_decompose to extract its components.
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm

# Create date range
index = pd.date_range(start='2020-01-01', periods=100, freq='M')
# Generate seasonal data
rng = np.random.RandomState(0)
y = np.sin(np.linspace(0, 4 * np.pi, 100)) + 0.5 * rng.randn(100)
series = pd.Series(y, index=index)

decomposition = sm.tsa.seasonal_decompose(series, model='additive')
print("Trend head:\n", decomposition.trend.dropna().head())
print("Seasonal head:\n", decomposition.seasonal.dropna().head())

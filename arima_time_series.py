"""
ARIMA Time Series Forecasting.

Box and Jenkins developed the ARIMA methodology in the 1970s for
modelling and forecasting time series. Here we generate synthetic
autoregressive data and fit an ARIMA(1,0,1) model using statsmodels.
"""

import numpy as np
import statsmodels.api as sm

rng = np.random.RandomState(0)
# Generate ARMA(1,1) process
ar_params = np.array([0.7])
ma_params = np.array([0.2])
ar = np.r_[1, -ar_params]  # add zero-lag and negate
ma = np.r_[1, ma_params]
y = sm.tsa.arma_generate_sample(ar, ma, nsample=200, scale=1, burnin=50)

# Fit ARIMA model
model = sm.tsa.arima.ARIMA(y, order=(1, 0, 1))
res = model.fit()

print(res.summary())

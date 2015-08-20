# Time series - Restaurant bookings

This dataset contains information about the number of bookings of 261 restaurants during the period 2011-11-14 to 2015-8-18. The goal of this competition is to be able to predict the number of bookings for B_t+1 given the number of bookings B_0...B_t. The evaluation metric used is the MSE for time series.

1 Fit the model to the data y_1,\dots,y_t and let \hat{y}_{t+1} denote the forecast of the next observation. Then compute the error (e_{t+1}^*=y_{t+1}-\hat{y}_{t+1}) for the forecast observation.

2 Repeat step 1 for t=m,\dots,n-1 where m is the minimum number of observations needed for fitting the model.

3 Compute the MSE from e_{m+1}^*,\dots,e_{n}^*.

from http://rob.yndman.com/hyndsight/crossvalidation/

## Results

jordicolomer_average {'n': 1} 15.3577523484

jordicolomer_average {'n': 2} 14.4347257415

jordicolomer_average {'n': 3} 14.2637135556

jordicolomer_average {'n': 4} 14.0159165157

jordicolomer_average {'n': 5} 13.5492501025

jordicolomer_average {'n': 6} 12.3986825592

jordicolomer_average {'n': 7} 10.6726869432

jordicolomer_average {'n': 8} 10.4966490339 ** Winner

jordicolomer_average {'n': 9} 10.9391933935

jordicolomer_average {'n': 10} 11.4215775311

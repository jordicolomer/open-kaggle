# Time series - Restaurant bookings

This dataset contains information about the number of bookings of 261 restaurants during the period 2011-11-14 to 2015-8-18. The goal of this competition is to be able to predict the number of bookings for B_t+1 given the number of bookings B_0...B_t. The evaluation metric used is the MSE for time series.

1 Fit the model to the data y_1,\dots,y_t and let \hat{y}_{t+1} denote the forecast of the next observation. Then compute the error (e_{t+1}^*=y_{t+1}-\hat{y}_{t+1}) for the forecast observation.

2 Repeat step 1 for t=m,\dots,n-1 where m is the minimum number of observations needed for fitting the model.

3 Compute the MSE from e_{m+1}^*,\dots,e_{n}^*.

from http://rob.yndman.com/hyndsight/crossvalidation/

## Results

jordicolomer_average 1 15.3577523484 

jordicolomer_average 2 14.4347257415 

jordicolomer_average 3 14.2637135556 

jordicolomer_average 4 14.0159165157 

jordicolomer_average 5 13.5492501025 

jordicolomer_average 6 12.3986825592 

jordicolomer_average 7 10.6726869432 

jordicolomer_average 8 10.4966490339 

jordicolomer_average 9 10.9391933935 

jordicolomer_average 10 11.4215775311 

jordicolomer_averageweekly 1 10.8443748688 

jordicolomer_averageweekly 2 9.09322754692 

jordicolomer_averageweekly 3 8.90418511883  ** New record!!

jordicolomer_averageweekly 4 9.18192794196 

jordicolomer_averageweekly 5 9.507487646 

jordicolomer_averageweekly 6 9.93895026521 

jordicolomer_averageweekly 7 10.3429477282 

jordicolomer_averageweekly 8 10.6762027153 

jordicolomer_averageweekly 9 10.9828834771 

jordicolomer_averageweekly 10 11.2569661696 

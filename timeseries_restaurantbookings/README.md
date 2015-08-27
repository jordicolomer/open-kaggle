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

jordicolomer_averageweekly 3 8.90418511883 

jordicolomer_averageweekly 4 9.18192794196 

jordicolomer_averageweekly 5 9.507487646 

jordicolomer_averageweekly 6 9.93895026521 

jordicolomer_averageweekly 7 10.3429477282 

jordicolomer_averageweekly 8 10.6762027153 

jordicolomer_averageweekly 9 10.9828834771 

jordicolomer_averageweekly 10 11.2569661696 

jordicolomer_averageWeeklyWithTrend 1 16.5751137913 

jordicolomer_averageWeeklyWithTrend 2 10.2166486348 

jordicolomer_averageWeeklyWithTrend 3 9.22347797614 

jordicolomer_averageWeeklyWithTrend 4 8.92978345885 

jordicolomer_averageWeeklyWithTrend 5 8.85736788148 

jordicolomer_averageWeeklyWithTrend 6 8.8177103795   ** New record!!

jordicolomer_averageWeeklyWithTrend 7 8.82209914972 

jordicolomer_averageWeeklyWithTrend 8 8.83118154665 

jordicolomer_averageWeeklyWithTrend 9 8.83936406557 

jordicolomer_averageWeeklyWithTrend 10 8.86448829165 

jordicolomer_averageWeeklyWithTrend 11 8.87222514113 

jordicolomer_averageWeeklyWithTrend 12 8.8890546831 

jordicolomer_averageWeeklyWithTrend 13 8.89110124166 

jordicolomer_averageWeeklyWithTrend 14 8.90003804482 

jordicolomer_averageWeeklyWithTrend 15 8.91692174372 

jordicolomer_averageWeeklyWithTrend 16 8.92380595429 

jordicolomer_averageWeeklyWithTrend 17 8.93474378542 

jordicolomer_averageWeeklyWithTrend 18 8.93438309104 

jordicolomer_averageWeeklyWithTrend 19 8.94598400753 

# Time series - Restaurant bookings

This dataset contains information about the number of bookings of 261 restaurants during the period 2011-11-14 to 2015-8-18. The goal of this competition is to be able to predict the number of bookings for B_t+1 given the number of bookings B_0...B_t. The evaluation metric used is the MSE for time series.

1 Fit the model to the data y_1,\dots,y_t and let \hat{y}_{t+1} denote the fore­cast of the next obser­va­tion. Then com­pute the error (e_{t+1}^*=y_{t+1}-\hat{y}_{t+1}) for the fore­cast observation.
2 Repeat step 1 for t=m,\dots,n-1 where m is the min­i­mum num­ber of obser­va­tions needed for fit­ting the model.
3 Com­pute the MSE from e_{m+1}^*,\dots,e_{n}^*.

* from http://rob.yndman.com/hyndsight/crossvalidation/

import pandas
import statsmodels as sm
import numpy as np
from statsmodels.tsa.ar_model import AR

def delete6keep1(x):
    ret = []
    for i in range(1, len(x)+1):
        #print x[-i], i%7==0
        if i%7==0:
            ret.insert(0, x[-i])
    return ret

def predict(x, params):
    x = delete6keep1(x)
    #x = range(10)
    try:
        model = AR(x)
        res = model.fit(maxlag=1)
        ret = int(res.predict(len(x), len(x))[0])
        if ret>100:
            print x,ret
        return ret
    except Exception, err:
        return 0

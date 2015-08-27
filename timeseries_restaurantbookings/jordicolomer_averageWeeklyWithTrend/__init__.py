def delete6keep1(x):
    ret = []
    for i in range(1, len(x)+1):
        #print x[-i], i%7==0
        if i%7==0:
            ret.insert(0, x[-i])
    return ret

def predict(x, params):
    x = delete6keep1(x)
    n = 3
    if 'n' in params:
        n = params['n']
    m = 10
    if 'm' in params:
        m = params['m']
    if len(x)<n:
        n=len(x)
    ret = sum(x[-n:])/n + (x[-1]-x[-3])/m
    #print x,sum(x[-n:])/n,(x[-1]-x[-3])/2, ret
    if ret < 0:
        ret = 0
    return ret

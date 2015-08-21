def delete6keep1(x):
    ret = []
    for i in range(1, len(x)+1):
        #print x[-i], i%7==0
        if i%7==0:
            ret.insert(0, x[-i])
    return ret

#print delete6keep1([6,'a',1,2,3,4,5,6,'b',1,2,3,4,5,6,'c',1,2,3,4,5,6,'d',1,2,3,4,5,6])

def predict(x, params):
    x = delete6keep1(x)
    n = 10
    if 'n' in params:
        n = params['n']
    if len(x)<n:
        n=len(x)
    return sum(x[-n:])/n

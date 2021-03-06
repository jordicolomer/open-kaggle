import dataset
import math

def trim(x, v):
    i = 0
    while x[i] == 0:
        i+=1
    return x[i:], v[i:]

def evaluate(row, alg, params):
    MSE = 0
    minsamples = 20
    n = 0
    for i in range(minsamples, len(row)-1):
        actual = row[i+1]
        params['dates'] = params['dates'][:i+1]
        prediction = alg(row[:i+1], params)
        MSE += math.pow(actual-prediction, 2)
        n += 1
    return MSE/n

def evaluate_all(ds, alg, params):
    MSE = 0
    n = 0
    for row in ds:
        #print n
        row, params['dates'] = trim(row, params['dates'])
        MSE += evaluate(row, alg, params)
        n += 1
    return MSE/n

def main():
    ds = dataset.load()
    dates = dataset.get_dates_array()
    import jordicolomer_autoregressive
    for m in range(1,2):
        params = {'m':m, 'dates':dates}
        print 'jordicolomer_autoregressive',m,evaluate_all(ds, jordicolomer_autoregressive.predict, params),'\n'
    #exit(0)
    import jordicolomer_average
    for n in range(1,11):
        params = {'n':n, 'dates':dates}
        print 'jordicolomer_average',n,evaluate_all(ds, jordicolomer_average.predict, params),'\n'
    import jordicolomer_averageweekly
    for n in range(1,11):
        params = {'n':n, 'dates':dates}
        print 'jordicolomer_averageweekly',n,evaluate_all(ds, jordicolomer_averageweekly.predict, params),'\n'
    import jordicolomer_averageWeeklyWithTrend
    for m in range(1,20):
        params = {'m':m, 'dates':dates}
        print 'jordicolomer_averageWeeklyWithTrend',m,evaluate_all(ds, jordicolomer_averageWeeklyWithTrend.predict, params),'\n'

main()

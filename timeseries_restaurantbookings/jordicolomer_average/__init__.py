def predict(x, params):
    n = 10
    if 'n' in params:
        n = params['n']
    return sum(x[-n:])/n

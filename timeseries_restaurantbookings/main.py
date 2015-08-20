import dataset
import math

def trim(x):
    i = 0
    while x[i] == 0:
        i+=1
    return x[i:]

dataset = dataset.load()

maxsum=0
for row in dataset:
    if sum(row)>maxsum:
        maxsum=sum(row)
        maxrow=row
row = trim(maxrow)

MSE = 0
import jordicolomer_average
minsamples = 20
n = 0
for i in range(minsamples, len(row)-1):
    actual = row[i+1]
    prediction = jordicolomer_average.predict(row[:i+1])
    MSE += math.pow(actual-prediction,2)
    n += 1
MSE = MSE/n
print MSE

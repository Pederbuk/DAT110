import pandas as pd
import scipy.stats as stats
df = pd.read_csv('startupcosts.csv',sep=';')
types_resturant = ['pizzarestaurant','bakery','shoestore','giftshop','petstore']
types_rest_mean = df.mean()
types_rest_sum = df.count()
types_rest_std = df.std()
n = df.stack().count()
total_mean = df.stack().mean()

sst = 0
ssg = 0
for rest in types_resturant:
    for value in df[rest]:
        sst += (value - total_mean) ** 2

    ssg += n * (types_rest_mean[rest] - total_mean) ** 2
sse = sst - ssg

dft = n-1
dfg = 5
dfe = dft-dfg


msg = ssg/dfg
mse = sse/dfe

F = msg/mse
p = stats.f.sf(F,dfg,dft)
print(p)
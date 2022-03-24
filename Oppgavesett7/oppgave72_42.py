import pandas as pd
import scipy.stats as stats
df = pd.read_csv('footballplayers.csv',sep=';')
teams = ['DallasCowboys', 'GreenBayPackers','DenverBroncos','MiamiDolphins','SanFransiscoFortyNiners']
teams_mean = df.mean()
teams_sum = df.count()
teams_std = df.std()
n = df.stack().count()
total_mean = df.stack().mean()

sst = 0
ssg = 0
for team in teams:
    for value in df[team]:
        sst += (value - total_mean)**2
    ssg += n*(teams_mean[team] - total_mean)**2
sse = sst - ssg

dft = n-1
dfg = 5
dfe = dft-dfg


msg = ssg/dfg
mse = sse/dfe

F = msg/mse
p = stats.f.sf(F,dfg,dft)
print(p)
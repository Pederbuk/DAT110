import pandas as pd
df = pd.read_csv('chickwts.csv',)
df_mean = df.groupby('feed').mean()
df_std = df.groupby('feed').std()
df_sum = df.groupby('feed').count()
df_total_mean = df['weight'].mean()

sst = 0
for value in df['weight']:
    sst += (value - df_total_mean)**2

ssg = 0
for mean, n in zip(df_mean['weight'],df_sum['weight']):
    ssg += n*(mean-df_total_mean)**2

sse = sst-ssg

dft = sum(df_sum['weight'])-1
dfg = 5
dfe = dft-dfg

msg = ssg/dfg
mse = sse/dfe

F = msg/mse

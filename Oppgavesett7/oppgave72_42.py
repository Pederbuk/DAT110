import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
df = pd.read_csv('footballplayers.csv',sep=';')

p = stats.f_oneway(df['DallasCowboys'],df['GreenBayPackers'],df['DenverBroncos'],df['MiamiDolphins'],df['SanFransiscoFortyNiners'])
print(p)

#betingelsene for anova?

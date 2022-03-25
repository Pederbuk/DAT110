import pandas as pd
import matplotlib.pyplot as plt

df_fb = pd.read_csv('footballplayers.csv',sep=';')
df_sk = pd.read_csv('startupcosts.csv',sep=';')


df_sk.boxplot()
df_fb.hist()
df_sk.hist()
plt.figure()

plt.show()
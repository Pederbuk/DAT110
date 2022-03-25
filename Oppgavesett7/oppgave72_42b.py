import pandas as pd
import scipy.stats as stats
from statsmodels.stats.multicomp import (pairwise_tukeyhsd,MultiComparison)
df = pd.read_csv('startupcosts.csv',sep=';')

p = stats.f_oneway(df['pizzarestaurant'],df['bakery'],df['shoestore'],df['giftshop'],df['petstore'])
print(p)

data_for_mc = df.stack().reset_index()
data_for_mc = data_for_mc.rename(columns={'level_o':id,'level_1':'Type_res', 0:'startkostnad'})

multiple_sammenlikninger = MultiComparison(data_for_mc['startkostnad'],data_for_mc['Type_res'])
print(multiple_sammenlikninger.tukeyhsd().summary())
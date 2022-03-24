import pandas as pd
import scipy.stats as stats
import math as m

def se(mse, n1,n2):
    return m.sqrt((mse/n1)+(mse/n2))

def t(mean1,mean2,se):
    return (mean1-mean2)/se

if __name__ =="__main__":

    df = pd.read_csv('chickwts.csv',)
    df_mean = df.groupby('feed').mean()
    df_std = df.groupby('feed').std()
    df_sum = df.groupby('feed').count()
    df_total_mean = df['weight'].mean()
    types_of_food = ['casein', 'horsebean','linseed','meatmeal','soybean','sunflower']
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
    p = stats.f.sf(F,dfg,dfe)

    string = f"""
    df, sum sq, mean sq, F-value, Pr
    {dfg}, {ssg:.2f}, {msg:.2f}, {F:.2f}  {p:.3f}
    {dfe}, {sse:.2f}, {mse:.2f}
    """
    print(string)

    p_values = {}
    p_values_less_a = {}
    for key in types_of_food:
        for key2 in types_of_food:
            if key != key2:
                s = f'{key2}_{key}'
                if s not in p_values.keys():
                    se_loop = se(mse, df_sum['weight'][key], df_sum['weight'][key2])
                    t_loop = t(df_mean['weight'][key], df_mean['weight'][key2], se_loop)
                    p_loop = stats.t.sf(abs(t_loop), dfe)*2
                    p_values[f'{key}_{key2}'] = p_loop
                    if p_loop < 3.33e-3:
                        p_values_less_a[f'{key}_{key2}'] = p_loop




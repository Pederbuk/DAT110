import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
data = pd.read_csv('possum.csv')

logmod = sm.logit(formula="pop ~ headL + skullW +totalL + tailL", data=data)
res = logmod.fit()
print(res.summary())

import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = pd.read_csv('babies.csv')
data = data.dropna()
x = data.drop(['case','bwt'],axis=1)
y = data['bwt']

regr = linear_model.LinearRegression()
regr.fit(x,y)

print(f'intercep = {regr.intercept_}, coefficients = {regr.coef_}')

x = sm.add_constant(x)
mlr = sm.OLS(y,x).fit()
print_mlr = mlr.summary()
print(print_mlr)

plt.figure()
plt.title('Histograms')
plt.subplot(231)
plt.hist(data['gestation'])
plt.subplot(232)
plt.hist(data['parity'])
plt.subplot(233)
plt.hist(data['age'])
plt.subplot(234)
plt.hist(data['weight'])
plt.subplot(235)
plt.hist(data['smoke'])
plt.show()

plt.figure()
plt.title('Scatter')
plt.subplot(231)
plt.scatter(data['bwt'], data['gestation'])
plt.subplot(232)
plt.scatter(data['bwt'], data['parity'])
plt.subplot(233)
plt.scatter(data['bwt'], data['age'])
plt.subplot(234)
plt.scatter(data['bwt'], data['weight'])
plt.subplot(235)
plt.scatter(data['bwt'], data['smoke'])
plt.show()





import pandas as pd

#reads the csv file and makes a dataframe
mammals_df = pd.read_csv('mammals.csv')

#calculates the standard deviation and variance
#both these calculations are normalised by N-1 to normalise by N set ddof=0
standard_deviation = mammals_df['body_wt'].std()
variance = mammals_df['body_wt'].var()
quantile_1 = mammals_df['body_wt'].quantile(0.25)
quartile_3 = mammals_df['body_wt'].quantile(0.75)
quartile_diffrenence = quartile_3 - quantile_1

print(f'Standard_deviation: {standard_deviation:.2f}')
print(f'Variance: {variance:.2f}')
print(f'Quartile_diffrence:{quartile_diffrenence:.2f}')


import pandas as pd

dataframe = pd.read_table('offshore_drilling.txt')

crosstable = pd.crosstab(dataframe.position,dataframe.college_grad,
                         margins=True, margins_name='Total')

print(crosstable)
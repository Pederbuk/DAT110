import numpy as np


normal_dist = np.random.normal(loc=1500,scale=300,size=100)
percentile = np.percentile(normal_dist,95)
print(f'the 95 percentile: {percentile:.2f}')

from scipy.stats import norm

# finner prosentandelen under 1800:
p = norm.cdf(1800,loc=1500,scale=300)
p = p*100
print(f'Andelen under Pam er: {p:.1f}%')


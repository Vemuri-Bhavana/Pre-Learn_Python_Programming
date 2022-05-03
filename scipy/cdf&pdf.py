from scipy.stats import norm

arr=norm.rvs(size=20) #rvs--random variables
norm.cdf(arr[10])
norm.pdf(arr[14])

'''Problem:
Use SciPy to declare 20 random values for random values and perform the following:
1. CDF – Cumulative Distribution Function for a random variable 10
2. PDF – Probability Density Function for a random variable 14.'''

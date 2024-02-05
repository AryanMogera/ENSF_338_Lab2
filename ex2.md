# Question 1

1. Interpolation search is more effective than binary search when datasets are more uniformly arranged or distriuted. This is because the algorithm instead of dividing the search space into two like binary search, it produces an estimate for the target values based on the intial and final elements in the data. 

2. Interpolation search allows variable jumps towards the estimated location of the target element in compariosn to the fixed jump that is done by the binary search that bifurcates its search space. This may have sub optimal results when data is skewed towards the extreme ends.

# Question 2

Certainly, the efficiency can be impacted when the assumption that the data is uniformly distributed doesn't hold true for a specific dataset. In the context of a normal distribution, where data tends to concentrate around the mean with a bell-shaped distribution towards the tails, it's crucial to recognize that interpolation search heavily relies on the minimum and maximum values within the dataset. To predict the target element, an optimized search path is determined. However, for this path to be truly optimized, the condition is that the input data must exhibit a uniform distribution. In cases where the data follows a normal distribution, there could be an increase in the number of search iterations, ultimately affecting the overall average case performance.

# Question 3 

The emphasized portion of the code, where the variable 'pos' is assigned, encapsulates the approach for locating the target element. It defines the strategy for dividing the data into two segments and subsequently seeks the target value along the most efficient search path.

'''python
pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))
'''

# Question 1

1. Interpolation search is more effective than binary search when datasets are more uniformly arranged or distriuted. This is because the algorithm instead of dividing the search space into two like binary search, it produces an estimate for the target values based on the intial and final elements in the data. 

2. Interpolation search allows variable jumps towards the estimated location of the target element in compariosn to the fixed jump that is done by the binary search that bifurcates its search space. This may have sub optimal results when data is skewed towards the extreme ends.

# Question 2

Certainly, the efficiency can be impacted when the assumption that the data is uniformly distributed doesn't hold true for a specific dataset. In the context of a normal distribution, where data tends to concentrate around the mean with a bell-shaped distribution towards the tails, it's crucial to recognize that interpolation search heavily relies on the minimum and maximum values within the dataset. To predict the target element, an optimized search path is determined. However, for this path to be truly optimized, the condition is that the input data must exhibit a uniform distribution. In cases where the data follows a normal distribution, there could be an increase in the number of search iterations, ultimately affecting the overall average case performance.

# Question 3 

The emphasized portion of the code, where the variable 'pos' is assigned, encapsulates the approach for locating the target element. It defines the strategy for dividing the data into two segments and subsequently seeks the target value along the most efficient search path.

```
 pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low]))) 
```


# Question 4

Linear search becomes our singular choice when presented with unsorted data or when efficient random access is not allowed. Here binary and interpolation will fail to do their job as they require sorted collection of data and prediction of the positions in the data. Linear search remains superior here having the ability to sequentially scan elements. 


# Question 5

In case where the given dataset is small and already sorted. Having the target element at the beginning helps linear search to have a small initial processing time than the other methods with more complex implementations.

# Question 6

Certainly we can implement algorithms to pre-sort the data before applying binary and interpolation search. Pre sorting takes more processing and computational capabilities. 




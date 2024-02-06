import timeit
import random

def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1

def binary_search(arr, target):
  low = 0
  high = len(arr) - 1

  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1 

  return -1

vector_sizes = [1000, 2000, 4000, 8000, 16000, 32000]


for size in vector_sizes:
    vector = sorted(random.sample(range(size * 10), size))

 
    total_linear_time = 0
    total_binary_time = 0
    for _ in range(1000):
      target = random.choice(vector)
      
      linear_time = timeit.timeit(lambda: linear_search(vector, target), number=100)

      binary_time = timeit.timeit(lambda: binary_search(vector, target), number=100)

      total_linear_time += linear_time
      total_binary_time += binary_time

    average_linear_time = total_linear_time / 1000
    average_binary_time = total_binary_time / 1000


    print(f"Vector size: {size}")
    print(f"Average time for linear search: {average_linear_time} seconds")
    print(f"Average time for binary search: {average_binary_time} seconds")
    print()

    import numpy as np
    from scipy.optimize import curve_fit

    def linear_func(x, a, b):
      return a * x + b

    def quadratic_func(x, a, b, c):
      return a * x**2 + b * x + c

    # Fit linear function
    linear_params, _ = curve_fit(linear_func, vector_sizes, [average_linear_time for _ in vector_sizes])

    # Fit quadratic function
    quadratic_params, _ = curve_fit(quadratic_func, vector_sizes, [average_linear_time for _ in vector_sizes])

    # Generate interpolated data points
    interpolated_linear = linear_func(vector_sizes, *linear_params)
    interpolated_quadratic = quadratic_func(vector_sizes, *quadratic_params)

    # Plot the interpolated data points
    import matplotlib.pyplot as plt

    plt.plot(vector_sizes, [average_linear_time for _ in vector_sizes], 'ro', label='Actual Data')
    plt.plot(vector_sizes, interpolated_linear, 'b-', label='Linear Interpolation')
    plt.plot(vector_sizes, interpolated_quadratic, 'g-', label='Quadratic Interpolation')
    plt.xlabel('Vector Size')
    plt.ylabel('Average Time (seconds)')
    plt.legend()
    plt.show()
import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

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



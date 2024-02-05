"""
1.This code is a simple example of a recursive function which calculates the nth number of the Fibonacci sequence.

2. Yes, it is an example of divide and conquer algorithm. The function func(n) divides the computation into two sub-problems, 
      func(n-1) and func(n-2), and then combines the results of the sub-problems to solve the original problem. 
      This is a characteristic of divide and conquer algorithms.

3. Time complexity- O(2^n), since there is a branching factor of 2, where each function call results in two more function calls.

5. Time complexity of the optimized algorithm is 0(n)
"""
import timeit
import matplotlib.pyplot as plt

def func(n):
  if n == 0 or n == 1:
    return n
  else:
    return func(n-1) + func(n-2)
def compute_time1():
  total_time = timeit.timeit(lambda: func(30), number=1)
  return total_time
  
memory ={}
def func1(n):
  if n in memory:
    return memory[n]
  if n <=2:
    fibo = 1
  else:
    fibo = func1(n-1) + func1(n-2)
    memory[n] = fibo
  return fibo

def compute_time2():
  total_time = timeit.timeit(lambda: func1(30), number=1)
  return total_time
  
               

print("Time taken by the first function is: ", compute_time1())
print("Time taken by the second function is: ", compute_time2())



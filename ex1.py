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
import numpy as np

def func(n):
  if n == 0 or n == 1:
    return n
  else:
    return func(n-1) + func(n-2)
  
nvalue= list(range(36))
timevalue = []

for n in nvalue:
  total_time= timeit.timeit(lambda: func(n), number =1)
  timevalue.append(total_time)

plt.plot(nvalue, timevalue)
plt.xlabel("n")
plt.ylabel("Time (sec)")
plt.title("n vs Time")
plt.savefig("ex1.6.1.jpg")
plt.show()  

memory ={}
def func1(n):
  if n in memory:
    return memory[n]
  else:
    if n <=2:
      fibo = 1
    else:
      fibo = func1(n-1) + func1(n-2)
      memory[n] = fibo
  return fibo

nvalue= list(range(35))
timevalue = []

for n in nvalue:
  total_time= timeit.timeit(lambda: func1(n), number =1)
  timevalue.append(total_time)

plt.plot(nvalue, timevalue)
plt.xlabel("n")
plt.ylabel("Time (sec)")
plt.title("n vs Time")

z= np.polyfit(nvalue, timevalue, 1)
p= np.poly1d(z)
plt.plot(nvalue, p(nvalue), label ="trend line", color = "red")

plt.legend
plt.savefig("ex1.6.2.jpg")
plt.show()  



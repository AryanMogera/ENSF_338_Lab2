'''
1. A profiler is a program that that provides profiling for programs. It provides a set of statistics that describes how often and 
    for how long various parts of the program is executed

2. Benchmarking answers the question how well a program performs while profiling helps you find where your application spends the 
    most time or consumes the most resources

4. From the two profiling of the two functions test_function() had 203 function calls (202 primitive calls) in 0.001 seconds
    and third_function() had 213 function calls (212 primitive calls) in 0.000 seconds. So execution time goes to the test_function

'''
import cProfile
import re
import timeit

def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
    
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data


def third_function():
#third function that calculates the source of the number from 0 to 999
    return [i**2 for i in range(100000000)]

test_function()
third_function()

cProfile.run('re.compile("test_function")')
cProfile.run('re.compile("third_function")')
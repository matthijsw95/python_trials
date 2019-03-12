import time
import numpy as np

runs = 10
fib_number = 999
times = {
    "fib": [],
    "smart_fib": [],
    "even_smarter_fib": []
}
memo = {}
second_memo = {}

def fib(n):
    if n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    return f

def smart_fib(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        f = 1
    else:
        f = smart_fib(n-1) + smart_fib(n-2)
    memo[n] = f
    return f

def run(func, x):
    time1 = int(round(time.time() * 1000))
    print func(x)
    time2 = int(round(time.time() * 1000))
    took = int(time2 - time1)
    times[func.__name__].append(took)
    return took

def even_smarter_fib(n):
    for k in range(1, n+1):
        if k <= 2:
            f = 1
        else: 
            f = second_memo[k-1] + second_memo[k-2]
        second_memo[k] = f
    return second_memo[n]


for i in range(runs):
    # print 'Run ' + str(i) + ' of ' + str(runs) + ' finished in + ' + str(run(fib, fib_number)) + ' milliseconds'
    print 'Run ' + str(i) + ' of ' + str(runs) + ' finished in + ' + str(run(smart_fib, fib_number)) + ' milliseconds'
    print 'Run ' + str(i) + ' of ' + str(runs) + ' finished in + ' + str(run(even_smarter_fib, fib_number)) + ' milliseconds'

# print 'Average for FIB: ' + str(np.mean(times['fib'])) + ' milliseconds'
print 'Average for SMART FIB: ' + str(np.mean(times['smart_fib'])) + ' milliseconds'
print 'Average for SMARTER FIB: ' + str(np.mean(times['even_smarter_fib'])) + ' milliseconds'

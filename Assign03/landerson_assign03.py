
"""
Coded by: Leyon Anderson
2/14/2026
COP3410 Assignment #3

Part 1:
    Plot the seven + 1 functions using matplotlib and overlay them.

Part 2:
    Sort a list of n items tracking the run times. Plot times and overlay O(n²).
"""

import matplotlib.pyplot as plt
import numpy as np
from time import time


def a_sort(values):
    '''
    Bubble sorts the list. O(n²)
    
    :param list values: List of random numbers to be sorted.
    '''
    for j in range(len(values)-1):
        for i in range(len(values)-(1+j)):
            if values[i] > values[i+1]:
                temp = values[i+1]
                values[i+1] = values[i]
                values[i] = temp 

    if len(values) == 100:
        print(values)
        print("Function does sort correctly.")

def fact(n):
    '''
    Quick recursive function to find the factorial of n.

    :param int n: Number to find the factorial of...
    :return int: Returns (n * n-1) or 1 if n <= 1
    '''
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)


if __name__ == "__main__":    
    """
    Part 1
    """
    # 1. Define the range for n (starting above 0 as log(0) is undefined)
    n = np.linspace(1, 10, 400)
    n_f = np.linspace(1, 10, 10)
    n_fact = [fact(n) for n in n_f]

    plt.figure(figsize=(10, 6))

    # 2. Calculate f(n) = log(n). np.log() is the natural log (base e)
    f_n = np.ones_like(n)
    plt.plot(n, f_n, label='f(n) = constant')
    f_n = n
    plt.plot(n, f_n, label='f(n) = n')
    f_n = np.log(n)
    plt.plot(n, f_n, label='f(n) = logn')
    f_n = n * np.log(n)
    plt.plot(n, f_n, label='f(n) = nlogn')
    f_n = n ** 2
    plt.plot(n, f_n, label='f(n) = n²')
    f_n = n ** 3
    plt.plot(n, f_n, label='f(n) = n³')
    f_n = 2 ** n
    plt.plot(n, f_n, label='f(n) = 2ⁿ')
    plt.plot(n_f, n_fact, label='f(n) = n!')

    # 3. Create the plot
    plt.legend()
    plt.xlim(2, 8)
    plt.yscale('log', base=2)
    plt.ylim(1, 4096)

    # 4. Add labels and a title
    plt.xlabel('n')
    plt.ylabel('f(n)')
    plt.title('Plot of f(n)')

    # 5. Show the result
    plt.show()

    """
    Part 2
    """
    run_time = []

    # Test n = 100
    rand_list = np.random.randint(low=0, high=100, size=100).tolist()
    start_time = time( ) # record the starting time
    a_sort(rand_list) #function call goes here
    end_time = time( ) # record the ending time
    elapsed = end_time - start_time
    run_time.append(elapsed)
    print("[X----]")

    # Test n = 1000
    rand_list = np.random.randint(low=0, high=100, size=1000).tolist()
    start_time = time( ) # record the starting time
    a_sort(rand_list) #function call goes here
    end_time = time( ) # record the ending time
    elapsed = end_time - start_time
    run_time.append(elapsed)
    print("[XX---]")

    # Test n = 3000
    rand_list = np.random.randint(low=0, high=100, size=3000).tolist()
    start_time = time( ) # record the starting time
    a_sort(rand_list) #function call goes here
    end_time = time( ) # record the ending time
    elapsed = end_time - start_time
    run_time.append(elapsed)
    print("[XXX--]")

    # Test n = 7500
    rand_list = np.random.randint(low=0, high=100, size=7500).tolist()
    start_time = time( ) # record the starting time
    a_sort(rand_list) #function call goes here
    end_time = time( ) # record the ending time
    elapsed = end_time - start_time
    run_time.append(elapsed)
    print("[XXXX-]")

    # Test n = 10000
    rand_list = np.random.randint(low=0, high=100, size=10000).tolist()
    start_time = time( ) # record the starting time
    a_sort(rand_list) #function call goes here
    end_time = time( ) # record the ending time
    elapsed = end_time - start_time
    run_time.append(elapsed)
    print("[XXXXX]")

    print(f'The run times to be plotted: {run_time}')
    # 1. Define the range for n (starting above 0 as log(0) is undefined)
    n = np.linspace(1, 10000, 10000) 
    n2 = [100, 1000, 3000, 7500, 10000]

    # 2. Calculate f(n) = log(n). np.log() is the natural log (base e)
    f_n = n ** 2
    plt.plot(n, f_n, label='O(n²)')
    plt.scatter(n2, run_time, label='run time')

    # 3. Create the plot
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')

    # 4. Add labels and a title
    plt.xlabel('n')
    plt.ylabel('time')
    plt.title('a_sort() Run Times')

    # 5. Show the result
    plt.show()
"""
Coded by: Leyon Anderson
Assignment #1
"""

def is_multiple(n, m):
    """
    R-1.1 Takes two integer values and returns True if n is a multiple of m, that is,
        n = mi for some integer i, and False otherwise.

    :param n: Integer
    :param m: Integer
    """
    if m % n == 0:
        return True
    return False

def is_even(k):
    '''
    R-1.2 Takes an integer value and returns True if k is even, and False otherwise. 
        However, this function cannot use the multiplication, modulo, or division 
        operators.
    
    :param k: Integer to test.
    '''
    return is_multiple(2, k)

def minmax(data):
    """
    R-1.3 Takes a sequence of one or more numbers, and returns the smallest and 
        largest numbers, in the form of a tuple of length two. Does not use the built-in 
        functions min or max.
    
    :param data: List of integers that is at least length 1.
    """
    min = data[0]
    max = data[0]

    for i in data:
        if i > max:
            max = i
        if i < min:
            min = i

    return min, max

def nSquare(n):
    """
    R-1.4 Takes a positive integer n and returns the sum of the squares of all 
        the positive integers smaller than n.

    :param n: Integer
    """
    sum = 0

    for x in range(1,n):
        sum += x * x
    
    return sum

def oddSquare(n):
    """
    R-1.6 Takes a positive integer n and returns the sum of the squares of all
        the odd positive integers smaller than n.

    :param n: Integer
    """
    sum = 0

    for x in range(1,n,2):
        sum += x * x
    
    return sum

"""
#Main
"""
print(is_multiple(2, 4)) # R-1.1
print(is_even(5)) # R-1.2
print(minmax((10, 2, 4, 11))) # R-1.3
print(nSquare(5)) # R-1.4

"""
R-1.5 Give a single command that computes the sum from Exercise R-1.4, 
relying on Python’s comprehension syntax and the built-in sum function.
"""
n = 5
print(sum([k*k for k in range(1, n)])) # R-1.5

print(oddSquare(6)) # R-1.6
"""
R-1.7 Give a single command that computes the sum from Exercise R-1.6, 
relying on Python’s comprehension syntax and the built-in sum function.
"""
n = 6
print(sum([k*k for k in range(1, n) if k % 2 != 0])) # R-1.7
"""
R-1.9 What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
"""
for x in range(50, 81, 10): # R-1.9
    print(x, end=' ')
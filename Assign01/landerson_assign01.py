
"""
Coded by: Leyon Anderson
1/23/2026
Assignment #1

There are 12 reinforcement exercises (page 51 Chapter 1 of the textbook, "Data Structures 
and Algorithms in Python" by Michael Goodrich et al.). Select 8 of those exercises and 
complete them. 
"""

def is_multiple(n, m):
    """
    Takes two integer values and returns True if n is a multiple of m, that is, n = mi for 
    some integer i, and False otherwise.

    :param int n: Denominator
    :param int m: Numerator
    :return bool: Result of the evaluation.
    """
    if m % n == 0:
        return True
    return False

def is_even(k):
    '''
    Takes an integer value and returns True if k is even, and False otherwise. However, this 
    function cannot use the multiplication, modulo, or division operators.
    
    :param int k: Number to evaluate.
    :return bool: Result of the evaluation.
    '''
    return is_multiple(2, k)

def minmax(data):
    """
    Takes a sequence of one or more numbers, and returns the smallest and largest numbers, 
    in the form of a tuple of length two. Does not use the built-in functions min or max.
    
    :param list data: List of integers that is at least length 1.
    :return tuple: Result as a tuple. (min, max)
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
    Takes a positive integer n and returns the sum of the squares of all the positive integers 
    smaller than n.

    :param int n: Number to evaluate.
    :return int: Result of the evaluation.
    """
    sum = 0

    for x in range(1,n):
        sum += x * x
    
    return sum

def nSquareL(n):
    """
    A single command that computes the sum from Exercise R-1.4, relying on Python’s 
    comprehension syntax and the built-in sum function.

    :param int n: Number to evaluate.
    :return int: Result of the evaluation.
    """
    return sum([k*k for k in range(1, n)])

def oddSquare(n):
    """
    Takes a positive integer n and returns the sum of the squares of all the odd positive 
    integers smaller than n.

    :param int n: Number to evaluate.
    :return int: Result of the evaluation.    
    """
    sum = 0

    for x in range(1,n,2):
        sum += x * x
    
    return sum

def oddSquareL(n):
    """
    A single command that computes the sum from Exercise R-1.6, relying on Python’s 
    comprehension syntax and the built-in sum function.

    :param int n: Number to evaluate.
    :return int: Result of the evaluation.    
    """
    return sum([k*k for k in range(1, n) if k % 2 != 0])

def quickRange():
    """
    The answer to the question in function form:

    What parameters should be sent to the range constructor, to produce a range with values 
    50, 60, 70, 80?
    """
    for x in range(50, 81, 10): # The answer. (Start: 50, End + 1: 81, Iteration: 10)
        print(x, end=' ')
    print("The answer: range(Start: 50, End + 1: 81, Iteration: 10)")

"""
#Main
"""
print(is_multiple(3, 10))        # R-1.1
print(is_even(12))               # R-1.2
print(minmax((11, 22, 5, 9)))   # R-1.3
print(nSquare(6))               # R-1.4
print(nSquareL(7))              # R-1.5
print(oddSquare(8))             # R-1.6
print(oddSquareL(9))            # R-1.7
quickRange()                    # R-1.9 Note this question has only 1 correct answer/output.
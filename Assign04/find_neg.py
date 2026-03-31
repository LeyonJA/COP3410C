
"""
Coded by: Leyon Anderson
3/28/2026
COP3410 Assignment #4

Goal is to design and implement a function to find all negative values within a 
given list. The function should output and return a new list containing the 
negative values.
"""

def fNeg(lst):
    '''
    Find all negative values within a list of integers.

    :param list lst: List of integers.
    '''
    return [x for x in lst if x < 0]

if __name__ == "__main__":
    print(fNeg([1, -1, -2, 3, 4])) # Function call contains the list to test.
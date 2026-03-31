
"""
Coded by: Leyon Anderson
3/28/2026
COP3410 Assignment #4

Uses the built-in sum function combined with Python’s comprehension syntax to 
compute the sum of all numbers in an N×N data set, represented as a list of lists.
"""

nxn = [[1, 2, 3],[1, 2, 3],[1, 2, 3]] # This is the list to test.

allSum = sum([sum(nxn[x]) for x in range(len(nxn))])
print(allSum)
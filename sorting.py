# -*- coding: utf-8 -*-
"""
Sorting Algorithms

"""

def selection_sort(A):
    '''
    sort by ascending order
    '''


    for i in range(1,len(A)):     #outer loop goes through the list
        for j in range(i,0,-1):   #inner loop moves to the left of the current value
            if A[j] < A[j-1]:     #Swap two values if out of order
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
    return A; 

data = [3, 1, 4, 9, 100, 12, 3, -2, 0]
data1 = ['f','a','u','o','w','l','s']
print(selection_sort(data1))



def insertion_sort(A):
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j>0 and A[j-1] > cur:
            
            A[j] = A[j-1]
            j-=1
        A[j] = cur
    return A
        

print(insertion_sort(data1))
